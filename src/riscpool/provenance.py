"""
Provenance ledger.

Every byte that enters data/ passes through fetch() and gets an immutable
record: exact URL, SHA256, byte size, UTC download time, and whatever
accession / release version identifies it upstream. Failures are recorded as
records too -- a 404 is a fact about the world, not a reason to invent a URL.
"""

import hashlib
import json
import os
import shutil
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(ROOT, "data")
RESULTS = os.path.join(ROOT, "results")
FIGURES = os.path.join(ROOT, "figures")
PROV_PATH = os.path.join(DATA, "PROVENANCE.json")

for _d in (DATA, RESULTS, FIGURES):
    os.makedirs(_d, exist_ok=True)


def utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            b = fh.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def _load():
    if os.path.exists(PROV_PATH):
        with open(PROV_PATH) as fh:
            return json.load(fh)
    return {"created_utc": utcnow(), "records": []}


def _save(led):
    led["updated_utc"] = utcnow()
    tmp = PROV_PATH + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(led, fh, indent=2, sort_keys=False)
    os.replace(tmp, PROV_PATH)


def _key(e):
    return (e.get("dataset"), e.get("path"), e.get("url"), e.get("sha256"),
            e.get("status"), e.get("kind"), e.get("error"))


def record(entry, dedupe=False):
    """Append a provenance record. With dedupe, an identical record is not
    appended twice, where identical means same dataset, path, url, hash,
    status, kind and error text. Re-running the build then leaves the ledger
    unchanged instead of growing it, which is what lets the generated report
    be reproducible. A URL that fails a NEW way still gets its own record,
    because the error text is part of the key."""
    led = _load()
    entry = dict(entry)
    entry.setdefault("recorded_utc", utcnow())
    if dedupe:
        k = _key(entry)
        for i, r in enumerate(led["records"]):
            if _key(r) == k:
                return r
    led["records"].append(entry)
    _save(led)
    return entry


def already(url):
    """Return an existing successful record for this URL if the local file is
    still present and its hash still matches. Downloads are idempotent."""
    led = _load()
    for r in led["records"]:
        if r.get("url") == url and r.get("status") == "OK":
            p = os.path.join(ROOT, r["path"])
            if os.path.exists(p) and os.path.getsize(p) == r["bytes"]:
                return r
    return None


def set_stability(path, stability, reason):
    """
    Annotate every record for `path` with whether its bytes are reproducible.

    Some sources are byte-stable: a deposited supplementary file, a GEO SOFT
    archive, a release FASTA. Re-fetching returns the same bytes and the
    SHA256 is a real check. Others are a server-side rendering of a page and
    return different bytes every time. Recording a hash for those and then
    asserting it would be a check that fails for a reason unrelated to the
    science, so they are marked here and verify.py reports them as
    not-hash-enforced instead of pretending either way.
    """
    led = _load()
    n = 0
    for r in led["records"]:
        if r.get("path") == path:
            r["content_stability"] = stability
            r["content_stability_reason"] = reason
            n += 1
    _save(led)
    return n


def fetch(url, dest, dataset, accession=None, version=None, note=None,
          timeout=1800, force=False, volatile=False):
    """
    Download url -> dest (path relative to repo root allowed). Records success
    or failure in data/PROVENANCE.json. Returns absolute path on success,
    None on failure. Never raises for network/HTTP problems.
    """
    dest_abs = dest if os.path.isabs(dest) else os.path.join(ROOT, dest)
    rel = os.path.relpath(dest_abs, ROOT)
    os.makedirs(os.path.dirname(dest_abs), exist_ok=True)

    if not force:
        prev = already(url)
        if prev is not None:
            print(f"[prov] cached  {rel}  ({prev['bytes']} B)")
            return os.path.join(ROOT, prev["path"])

    t0 = time.time()
    started = utcnow()
    tmp = dest_abs + ".part"
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "riscpool-build/1.0 (research)"})
        with urllib.request.urlopen(req, timeout=timeout) as resp, \
                open(tmp, "wb") as out:
            code = getattr(resp, "status", 200)
            shutil.copyfileobj(resp, out, length=1 << 20)
        os.replace(tmp, dest_abs)
        entry = {
            "dataset": dataset,
            "status": "OK",
            "url": url,
            "path": rel,
            "bytes": os.path.getsize(dest_abs),
            "sha256": sha256_file(dest_abs),
            "http_status": code,
            "download_started_utc": started,
            "download_finished_utc": utcnow(),
            "elapsed_s": round(time.time() - t0, 3),
            "accession": accession,
            "version": version,
            "note": note,
            "content_stability": "volatile" if volatile else "byte_stable",
        }
        record(entry)
        print(f"[prov] OK      {rel}  {entry['bytes']} B  "
              f"sha256={entry['sha256'][:16]}...  {entry['elapsed_s']}s")
        return dest_abs
    except Exception as exc:
        if os.path.exists(tmp):
            os.remove(tmp)
        http_status = getattr(exc, "code", None)
        entry = {
            "dataset": dataset,
            "status": "FAILED",
            "url": url,
            "path": rel,
            "bytes": None,
            "sha256": None,
            "http_status": http_status,
            "download_started_utc": started,
            "download_finished_utc": utcnow(),
            "elapsed_s": round(time.time() - t0, 3),
            "accession": accession,
            "version": version,
            "note": note,
            "error": f"{type(exc).__name__}: {exc}",
        }
        record(entry, dedupe=True)
        print(f"[prov] FAILED  {url}\n         {entry['error']}")
        return None


def fetch_first(candidates, dest, dataset, accession=None, version=None,
                note=None):
    """Try candidate URLs in order. Every failure is recorded before the next
    candidate is attempted. Returns (path, url) or (None, None)."""
    for url in candidates:
        p = fetch(url, dest, dataset, accession=accession, version=version,
                  note=note)
        if p is not None:
            return p, url
    return None, None


def register_local(path, dataset, note=None, source=None):
    """Record a file that was produced locally (derived artifact) so that it
    is hashed and traceable alongside the downloads.

    A derived file is superseded by path, not appended to. dedupe keys on the
    hash, so when a derived artifact legitimately changes, for instance
    because a bug in the feature pipeline was fixed, dedupe appends a second
    record and leaves the first one pointing at content that no longer
    exists. Stage A then re-hashes both and one of them must fail, which
    reports a stale ledger as a data-integrity failure. Downloads keep the
    append behaviour, because a URL that fails a new way is genuinely a new
    fact; a derived file has only a current state."""
    ab = path if os.path.isabs(path) else os.path.join(ROOT, path)
    rel = os.path.relpath(ab, ROOT)
    entry = {
        "dataset": dataset,
        "status": "OK",
        "kind": "derived",
        "url": source,
        "path": rel,
        "bytes": os.path.getsize(ab),
        "sha256": sha256_file(ab),
        "note": note,
    }
    led = _load()
    entry["recorded_utc"] = utcnow()
    keep = [r for r in led["records"]
            if not (r.get("kind") == "derived" and r.get("path") == rel)]
    if len(keep) != len(led["records"]):
        # only rewrite the timestamp when something actually changed, so a
        # no-op rebuild leaves the ledger byte-identical
        prior = [r for r in led["records"]
                 if r.get("kind") == "derived" and r.get("path") == rel]
        if len(prior) == 1 and _key(prior[0]) == _key(entry):
            return prior[0]
    led["records"] = keep + [entry]
    _save(led)
    return entry

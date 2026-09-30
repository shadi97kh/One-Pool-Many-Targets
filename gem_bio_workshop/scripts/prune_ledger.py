"""
Reconcile data/PROVENANCE.json with the tree it describes.

Two kinds of stale record accumulate, both only for DERIVED artifacts:

  * duplicates. register_local used to append when a derived file changed
    rather than replace, so a file that was legitimately regenerated left a
    record pointing at content that no longer exists. That is fixed at source
    now; this removes the ones already written.
  * orphans. Figures were renamed in an earlier refactor and the records for
    the old names were never removed, so stage A was being asked to hash
    files that cannot exist.

Downloaded records are never touched, including failures: a failed retrieval
is a real result and the ledger is the only place it is written down.

    python3 scripts/prune_ledger.py --dry-run
    python3 scripts/prune_ledger.py
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool.provenance import PROV_PATH, ROOT, utcnow      # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    led = json.load(open(PROV_PATH))
    records = led["records"]

    # keep only the LAST derived record for each path, and only if the file
    # is actually there
    last_derived = {}
    for i, r in enumerate(records):
        if r.get("kind") == "derived" and r.get("path"):
            last_derived[r["path"]] = i

    keep, dropped = [], []
    for i, r in enumerate(records):
        if r.get("kind") != "derived":
            keep.append(r)
            continue
        path = r.get("path")
        if path is None:
            keep.append(r)
            continue
        if last_derived.get(path) != i:
            dropped.append((r, "superseded by a later record for the same "
                               "path"))
            continue
        if not os.path.exists(os.path.join(ROOT, path)):
            dropped.append((r, "derived file no longer exists; renamed or "
                               "removed"))
            continue
        keep.append(r)

    print(f"records: {len(records)} -> {len(keep)}  ({len(dropped)} dropped)")
    for r, why in dropped:
        print(f"  drop {r['path']}  [{why}]")
    if args.dry_run:
        print("dry run; nothing written")
        return 0
    if not dropped:
        print("nothing to do")
        return 0
    led["records"] = keep
    led["pruned_utc"] = utcnow()
    led["prune_note"] = (
        "derived records reconciled against the tree: superseded duplicates "
        "and records for renamed or removed derived files were dropped. "
        "Downloaded records, including failures, are never pruned.")
    tmp = PROV_PATH + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(led, fh, indent=2)
    os.replace(tmp, PROV_PATH)
    print(f"wrote {PROV_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

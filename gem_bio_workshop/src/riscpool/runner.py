"""
Experiment harness.

Every experiment is a function returning a dict of values. The harness writes
results/<name>.json and nothing else in the repository is allowed to report a
number. On exception the harness writes status FAILED with the full traceback,
prints loudly, and returns -- the caller continues to the next experiment.
A failed experiment is a real result and is reported as one.
"""

import json
import os
import time
import traceback

import numpy as np

from .provenance import RESULTS, utcnow


def jsonify(o):
    """Make numpy / torch scalars and arrays JSON-safe without rounding."""
    import numbers
    if o is None or isinstance(o, (str, bool)):
        return o
    if isinstance(o, numbers.Integral):
        return int(o)
    if isinstance(o, numbers.Real):
        v = float(o)
        if np.isnan(v):
            return None
        if np.isinf(v):
            return "Infinity" if v > 0 else "-Infinity"
        return v
    if isinstance(o, dict):
        return {str(k): jsonify(v) for k, v in o.items()}
    if isinstance(o, (list, tuple, set)):
        return [jsonify(v) for v in o]
    if isinstance(o, np.ndarray):
        return jsonify(o.tolist())
    if hasattr(o, "detach"):
        return jsonify(o.detach().cpu().numpy())
    if hasattr(o, "item"):
        try:
            return jsonify(o.item())
        except Exception:
            pass
    return str(o)


def result_path(name):
    return os.path.join(RESULTS, f"{name}.json")


def scrub_paths(o, root=None):
    """
    Replace the absolute repository path with a relative one, everywhere.

    Result files record where their outputs went, and os.path.join gives an
    absolute path, which on a personal machine embeds the user's name. That is
    fine locally and is a de-anonymisation leak the moment the results are
    attached to a double-blind submission. Scrubbing here, at the one place
    every result is written, means no experiment has to remember to do it and
    no future experiment can reintroduce it.
    """
    from .provenance import ROOT
    root = (root or ROOT).rstrip("/") + "/"
    if isinstance(o, str):
        return o.replace(root, "")
    if isinstance(o, dict):
        return {k: scrub_paths(v, root) for k, v in o.items()}
    if isinstance(o, list):
        return [scrub_paths(v, root) for v in o]
    return o


def write_result(name, status, values, seed, elapsed_s, tb=None, meta=None):
    payload = {
        "name": name,
        "status": status,
        "values": jsonify(values if values is not None else {}),
        "seed": jsonify(seed),
        "elapsed_s": round(float(elapsed_s), 4),
        "traceback": tb,
        "timestamp_utc": utcnow(),
    }
    if meta:
        payload["meta"] = jsonify(meta)
    payload = scrub_paths(payload)
    tmp = result_path(name) + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(payload, fh, indent=2)
    os.replace(tmp, result_path(name))
    return payload


def run(name, fn, seed=0, meta=None, **kwargs):
    """
    Run experiment `fn`, writing results/<name>.json exactly once.
    Returns the payload dict. Never raises.
    """
    bar = "=" * 72
    print(f"\n{bar}\n[run] {name}   seed={seed}   {utcnow()}\n{bar}", flush=True)
    t0 = time.time()
    try:
        values = fn(seed=seed, **kwargs)
        el = time.time() - t0
        p = write_result(name, "OK", values, seed, el, None, meta)
        print(f"[run] {name}  status=OK  elapsed={el:.2f}s", flush=True)
        return p
    except BaseException:
        el = time.time() - t0
        tb = traceback.format_exc()
        print("\n" + "!" * 72, flush=True)
        print(f"!!! EXPERIMENT FAILED: {name}   after {el:.2f}s", flush=True)
        print("!" * 72, flush=True)
        print(tb, flush=True)
        print("!" * 72 + "\n", flush=True)
        p = write_result(name, "FAILED", {}, seed, el, tb, meta)
        return p


def load_result(name):
    p = result_path(name)
    if not os.path.exists(p):
        return None
    with open(p) as fh:
        return json.load(fh)


def load_all():
    out = {}
    for fn in sorted(os.listdir(RESULTS)):
        if fn.endswith(".json") and not fn.startswith("verify_"):
            with open(os.path.join(RESULTS, fn)) as fh:
                out[fn[:-5]] = json.load(fh)
    return out

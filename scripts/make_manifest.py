"""MANIFEST.json: environment, seeds, timings and a hash of every build
artifact -- source, experiment scripts, results, TeX, figures and the PDF."""
import json
import os
import platform
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from riscpool.provenance import ROOT, utcnow, sha256_file   # noqa: E402
from riscpool.runner import load_all                        # noqa: E402


def sh(cmd):
    try:
        return subprocess.run(cmd, shell=True, capture_output=True, text=True,
                              cwd=ROOT, timeout=180).stdout.strip()
    except Exception as e:
        return f"<unavailable: {e}>"


def hash_tree(root, subdir, suffixes):
    """SHA256 every file of the given kinds under a directory, sorted.

    A manifest that hashes only the result files can say the results have not
    changed while the code that produced them, the figures drawn from them and
    the manuscript that quotes them have all moved underneath. Hashing the
    whole build closes that gap: source, experiment scripts, results, TeX,
    figures and the compiled PDF.
    """
    base = os.path.join(root, subdir)
    out = {}
    if not os.path.isdir(base):
        return out
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in sorted(dirnames)
                       if d not in ("__pycache__", ".git")]
        for fn in sorted(filenames):
            if not fn.endswith(tuple(suffixes)):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, root)
            out[rel] = {"sha256": sha256_file(full),
                        "bytes": os.path.getsize(full)}
    return out


def main():
    res = load_all()
    seeds, wall = {}, {}
    for name, r in res.items():
        seeds[name] = r.get("seed")
        wall[name] = r.get("elapsed_s")
    freeze = sh(f"{sys.executable} -m pip freeze")

    def redact(line):
        """Strip install URLs while keeping the package identity.

        pip freeze emits three forms: "name==version", "name @ file:///path"
        for local installs, and "-e vcs+url#egg=name" for editable ones. The
        last two carry a filesystem or repository path that on a personal
        machine names the account holder, which is a de-anonymisation leak in
        a double-blind submission. The package name is what reproducibility
        needs, so it is kept and only the location is dropped."""
        if "://" not in line:
            return line
        if line.startswith("-e ") and "#egg=" in line:
            return f"-e <url redacted>#egg={line.rsplit('#egg=', 1)[-1]}"
        if " @ " in line:
            return f"{line.split(' @ ', 1)[0]} @ <url redacted>"
        return "<url redacted>"

    freeze_lines = [redact(x) for x in freeze.splitlines()]
    n_redacted = sum(1 for a, b in zip(freeze.splitlines(), freeze_lines)
                     if a != b)
    man = {
        "generated_utc": utcnow(),
        "git_commit": sh("git rev-parse HEAD"),
        "git_branch": sh("git rev-parse --abbrev-ref HEAD"),
        "git_status_porcelain": sh("git status --porcelain"),
        "python_version": sys.version,
        "python_version_short": platform.python_version(),
        "python_executable": sys.executable,
        "platform": platform.platform(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "pip_freeze": freeze_lines,
        "n_pip_entries_redacted": n_redacted,
        "redaction_note": ("editable/VCS install URLs are redacted because "
                           "they embed the account holder's name"),
        "seeds": seeds,
        "wall_clock_seconds_per_experiment": wall,
        "total_experiment_wall_clock_seconds": round(
            sum(v for v in wall.values() if isinstance(v, (int, float))), 3),
        "experiment_status": {k: v.get("status") for k, v in res.items()},
        "n_experiments": len(res),
        "n_failed": sum(1 for v in res.values() if v.get("status") == "FAILED"),
        "results_files": {
            k: {"sha256": sha256_file(os.path.join(ROOT, "results",
                                                   f"{k}.json")),
                "bytes": os.path.getsize(os.path.join(ROOT, "results",
                                                      f"{k}.json"))}
            for k in res},
        "source_files": hash_tree(ROOT, "src", (".py",)),
        "script_files": hash_tree(ROOT, "scripts", (".py",)),
        "verifier_file": {
            "verify.py": {
                "sha256": sha256_file(os.path.join(ROOT, "verify.py")),
                "bytes": os.path.getsize(os.path.join(ROOT, "verify.py"))}},
        "tex_files": hash_tree(ROOT, "paper", (".tex", ".bib", ".sty")),
        "figure_files": hash_tree(ROOT, "figures",
                                  (".pdf", ".png", ".md", ".json")),
        "pdf_file": ({"paper/main.pdf": {
            "sha256": sha256_file(os.path.join(ROOT, "paper", "main.pdf")),
            "bytes": os.path.getsize(os.path.join(ROOT, "paper", "main.pdf"))}}
            if os.path.exists(os.path.join(ROOT, "paper", "main.pdf"))
            else {}),
        "hashing_note": (
            "every artifact of the build is hashed, not only the results: "
            "source, experiment scripts, the verifier, TeX sources, figures "
            "and the compiled PDF. paper/ is not tracked in version control, "
            "so its hashes are the only record that a given manuscript "
            "corresponds to a given set of results."),
        "build_is_clean": not bool(sh("git status --porcelain")),
        "clean_state_note": (
            "build_is_clean is false if the working tree had uncommitted "
            "changes when this manifest was written, in which case "
            "git_commit does NOT fully describe the build and the file "
            "hashes above are the authoritative record."),
    }
    p = os.path.join(ROOT, "MANIFEST.json")
    with open(p, "w") as fh:
        json.dump(man, fh, indent=2)
    print(f"wrote {p}  ({man['n_experiments']} experiments, "
          f"{man['n_failed']} failed)")


if __name__ == "__main__":
    main()

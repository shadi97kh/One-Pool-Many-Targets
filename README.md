# One Pool, Many Targets

Experiments, saved results and figures for GEM bio workshop submission 101,
*One pool, many targets*.

The workshop is isolated in [`gem_bio_workshop/`](gem_bio_workshop/GUIDE.md):

- [Figure and experiment map](gem_bio_workshop/FIGURE_MAP.md): all 11 numbered figures, both tables, and supplementary experiments.
- [Source code](gem_bio_workshop/src/riscpool/) and [experiment runners](gem_bio_workshop/scripts/).
- [Saved results](gem_bio_workshop/results/) and [figures](gem_bio_workshop/figures/).
- [Reproduction guide](gem_bio_workshop/GUIDE.md), [snapshot manifest](gem_bio_workshop/EXTRACTION_MANIFEST.json), and [validation](gem_bio_workshop/VALIDATION.json).

The 154 historical files come from GEM's September 7, 2026 workshop snapshot.
The original bisection implementation is preserved. AISTATS experiments and later
shared-code changes remain in the separate [GEM repository](https://github.com/shadi97kh/RISCPOOL_GEM).

```bash
cd gem_bio_workshop
python3 verify_snapshot.py
```

Raw datasets and manuscript builds are excluded; the folder includes download
scripts, source URLs and hashes. See the reproduction guide for scientific
requirements and commands.

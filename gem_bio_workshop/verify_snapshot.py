#!/usr/bin/env python3
"""Verify the workshop export without downloads or scientific dependencies."""
import ast
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent


def main():
    manifest = json.loads((ROOT / 'EXTRACTION_MANIFEST.json').read_text())
    errors = []
    historical = manifest['historical_files']
    if len(historical) != manifest['historical_file_count']:
        errors.append('Historical file count does not match the manifest')
    for name, expected in historical.items():
        path = ROOT / name
        if not path.is_file():
            errors.append(f'Missing historical file: {name}')
            continue
        content = path.read_bytes()
        if len(content) != expected['bytes']:
            errors.append(f'Size changed: {name}')
        if hashlib.sha256(content).hexdigest() != expected['sha256']:
            errors.append(f'Content changed: {name}')
        if path.suffix == '.py':
            try:
                ast.parse(content, filename=name)
            except SyntaxError as exc:
                errors.append(f'Python syntax: {name}: {exc}')
    figures = json.loads((ROOT / 'figure_map.json').read_text())
    if sorted(item['submission_figure'] for item in figures) != list(range(1, 12)):
        errors.append('Figure map must contain submission Figures 1 through 11')
    for item in figures:
        refs = item['assets'] + item['results'] + item['experiment_scripts']
        if item['plot_script']:
            refs.append(item['plot_script'])
        for name in refs:
            if not (ROOT / name).is_file():
                errors.append(f"Figure {item['submission_figure']} is missing {name}")
    for name in historical:
        if name.startswith('results/') and name.endswith('.json'):
            try:
                result = json.loads((ROOT / name).read_text())
            except (OSError, ValueError) as exc:
                errors.append(f'Cannot read result {name}: {exc}')
                continue
            if isinstance(result, dict) and result.get('status') == 'FAILED':
                errors.append(f'Failed archived result: {name}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(historical)} historical files match {manifest['source_commit'][:12]}; "
          'all 11 submission figures resolve; archived Python source parses.')
    print('This checks the export; it does not rerun scientific experiments.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

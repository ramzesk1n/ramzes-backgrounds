# Local performance benchmark

Measured on 2026-10-15T18:27:12Z with Python 3.12.14 on Linux.

These are file-operation timings from this environment. They include Python process startup, JSON parsing, and file access. They exclude network transfer, AI inference, choosing a design, and editing or testing a website. They are not a guarantee for another machine.

| Operation | Median | Range |
| --- | ---: | ---: |
| niche lookup | 73.84 ms | 65.52–110.50 ms |
| guide lookup | 73.30 ms | 60.59–126.20 ms |
| filtered list | 89.07 ms | 74.97–183.32 ms |
| recipe lookup | 128.22 ms | 72.52–151.15 ms |
| export technical-grid | 125.76 ms | 72.72–178.60 ms |
| export microcement | 134.19 ms | 66.96–146.95 ms |
| export latte-uniform-photo | 121.53 ms | 80.72–146.00 ms |
| install claude | 254.52 ms | One run |
| install codex | 206.88 ms | One run |

Lookup and export operations ran seven times sequentially. Each export used a new empty directory and semantic tokens. Each installed agent skill successfully queried all 372 repeating recipes and exported a recipe from its own bundled assets. Existing-installation overwrite protection passed for both agents.

## What to expect in a project

The exporter typically finishes well below one second on this machine. The agent spends most of its time reading the site palette, comparing candidates, editing the section, and verifying the result. Practical planning estimates, not measured agent benchmarks:

- Known recipe and clear palette: roughly 1–3 minutes to export and integrate.
- Selection among three candidates and palette mapping: roughly 3–7 minutes.
- Integration with responsive and browser checks: roughly 5–15 minutes.

Actual time depends on the model, site size, build tools, browser access, and any conflicts found. First-time cloning depends on the connection and is separate from these estimates. No new image is generated for an existing recipe.

## Example output size

| Recipe | CSS | CSS gzip | Referenced image assets |
| --- | ---: | ---: | ---: |
| technical-grid | 1088 B | 509 B | 0 B |
| microcement | 1086 B | 510 B | 40,903 B |
| latte-uniform-photo | 1129 B | 525 B | 160,400 B |

Image asset bytes include all exported desktop/mobile dependencies. A browser chooses the appropriate image; this is not a measured per-page network transfer. The catalog and its JavaScript are not exported to client sites.

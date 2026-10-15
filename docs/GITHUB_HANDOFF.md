# GitHub distribution

Repository: https://github.com/ramzesk1n/ramzes-backgrounds

The public Git checkout contains a compressed working library with all runtime assets, all 500 recipes, full source files, and self-contained skills for Claude Code and Codex. The English README, Russian documentation, and Python entry points are also available as normal files. Original PNG masters remain in the separate archival package.

The entry points verify the versioned package's SHA-256 and unpack it into a local `.runtime/` directory on first use. Subsequent commands reuse that copy. No GitHub workflow or server-side automation is required for installation or export.

Use `python3 scripts/build_gallery.py` to create the standalone offline HTML catalog from the existing files. This requires only Python 3; it does not regenerate any images or require source PNG files.

Use `python3 scripts/install_skill.py --target claude --user` or the corresponding `--target codex` command to install once for your projects. The installed skill and exported backgrounds work independently of the checkout.

Validation covers all 500 standard exports, 12 accent variants, 16 neon variants, token bindings, asset isolation, checksums, overwrite protection, and gallery JavaScript syntax. See QA.md for the limits of these checks. Local lookup, export and installation timings are in BENCHMARK.md; agent integration estimates are not measured model benchmarks.

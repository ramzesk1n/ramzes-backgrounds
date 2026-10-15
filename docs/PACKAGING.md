# Package format

The public checkout includes `ramzes-backgrounds-1.1.0.tar.xz` (13,171,912 bytes) and small Python entry points. The archive contains the complete working source tree: 2,155 files, all 500 recipes, 520 runtime assets, and the portable agent skill. Original PNG masters stay in the separate archival package.

Before first use, the entry point verifies the archive's SHA-256 from `library.json`, checks archive paths, unpacks to a versioned local cache, and verifies card count and version. Later calls reuse the cache. The installed skill is a self-contained copy and does not depend on this cache or checkout.

`python3 scripts/build_gallery.py` produces a self-contained root `index.html`. `scripts/backgrounds.py` and `scripts/install_skill.py` retain the CLI of the source distribution. All setup and export operations run locally and require no server automation.

Updates arrive through `git pull --ff-only`. A new package checksum creates a new runtime cache. Previously installed skills and client exports are not replaced automatically.

The first unpack and query measured 0.656 seconds in this environment; a cached export measured 0.117 seconds. See PACKAGING_VALIDATION.json for verification and BENCHMARK.md for the separate source-export benchmark and estimated agent work time.

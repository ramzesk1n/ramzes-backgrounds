# Ramzes Backgrounds

**500 static website backgrounds, a visual catalog, and a portable skill for Claude Code and Codex.**

Browse materials by business niche, select a recipe, bind it to your design tokens, and export only the files your website needs. Exported backgrounds use CSS, SVG, or WebP with zero client-side JavaScript.

The complete working library is stored in a **13.2 MB compressed package** in this repository. Python entry points verify its SHA-256 and unpack it locally on first use. Later commands reuse the local copy. All 500 recipes, their source files, SVG/WebP assets, and the portable agent skill are included; no download or image generation is needed after cloning.

Version **1.1.0** includes **107 curated niche guides**. The visual catalog merges overlapping guide names and material tags into **138 unique niche options**.

[Russian documentation](README.ru.md) · [Design tokens](docs/TOKENS.md) · [Quality checks](docs/QA.md) · [Asset provenance](ASSET_ORIGINS.md)

## Quick start

Clone the repository once on the computer or VPS where your coding agent runs:

```bash
git clone --depth 1 https://github.com/ramzesk1n/ramzes-backgrounds.git
cd ramzes-backgrounds
```

On Windows, use `python` in place of `python3` if that is your Python command.

### Browse the catalog

Build the offline catalog from the existing recipes and assets:

```bash
python3 scripts/build_gallery.py
```

Then open `index.html` in your browser. It is self-contained and works offline. You can filter by niche, material family, rendering technology, placement, coverage, style, or era; change colors and intensity; inspect a 3×3 repeat; and copy CSS or download an HTML example. The generated HTML is excluded from Git; installing and using the skill does not require this build step.

If your browser restricts local downloads, serve the checkout locally:

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080`. The catalog UI is currently in Russian; recipe IDs and CLI commands use English.

### Install the agent skill

For all your projects, run the command for your agent:

```bash
python3 scripts/install_skill.py --target claude --user
python3 scripts/install_skill.py --target codex --user
```

For a project-only installation, replace `--user` with `--project /absolute/path/to/site`.

Start a new agent session in your website project. Invoke `/ramzes-backgrounds` in Claude Code or `$ramzes-backgrounds` in Codex, then describe the site, section, and desired material. For example:

> Use the existing design tokens. Suggest three restrained backgrounds for an apartment renovation website and explain their tradeoffs. After I choose one, export and integrate it into the hero. Check text contrast, mobile layout, asset URLs, and pseudo-element conflicts.

If you already chose a recipe, give its ID and ask the agent to integrate it directly. The skill, metadata, exporter, and assets are installed together. Selection and export work locally without MCP, a paid API, or image generation.

The installer preserves an existing installation. It will refuse to overwrite that folder.

## Use the CLI directly

Only Python 3 and its standard library are required to select and export existing recipes.

```bash
python3 scripts/backgrounds.py niches --query windows
python3 scripts/backgrounds.py guide windows
python3 scripts/backgrounds.py list --tech SVG --seamless
python3 scripts/backgrounds.py show microcement
python3 scripts/backgrounds.py export microcement \
  --out /absolute/path/to/site/public/backgrounds/microcement \
  --tokens /absolute/path/to/site/design-system/background-tokens.json \
  --intensity 0.4
```

The output directory must be new or empty and outside the library checkout. Each export includes `background.css`, only the referenced assets, a standalone `example.html`, a preview-only theme stylesheet, a license, and `background.lock.json` with version, parameters, token bindings, and file hashes.

Connect `background.css` to your site and apply `rb-surface` to the decorative section. Keep the CSS and its `assets` directory together, or adjust URLs for your build system. For multiple recipes on a page, give each recipe a unique class throughout its CSS.

## Follow the website palette

Read the site's existing design tokens before exporting. Map semantic roles to the real CSS variable names:

```json
{
  "tokens": {
    "primary": "#38534a",
    "background": "#f5f1e8"
  },
  "bindings": {
    "primary": "--color-brand-primary",
    "background": "--color-page-background"
  }
}
```

Exported CSS preserves live `var(--your-token, fallback)` bindings. Changing the site's theme updates the linked colors without another export. Review the recipe's `token_roles` and supply the colors it uses. Full-color WebP materials retain their original image colors.

Adjust `--rb-intensity`, `--rb-scale`, and `--rb-position` for the section. The usual recipe uses `::before`; optional neon also uses `::after`. Check that these pseudo-elements are available. Keep the content readable and test repeat seams for repeating materials.

Use `theme-example.css` only with the standalone example. It is not a replacement for the website's design system.

## Collection

| Technology | Recipes |
| --- | ---: |
| CSS | 61 |
| SVG | 381 |
| WebP | 58 |
| **Total** | **500** |

Placement: **372 repeat**, **114 cover**, **14 overlay**. Coverage: **466 full surfaces** and **34 accents**. Twelve recipes have an alternative accent composition; sixteen support optional static neon. WebP materials include desktop and mobile files.

Materials include paper, minerals, wood, textiles, metals, leather, plastics, food, liquids, natural patterns, optics, and industrial graphics. Niche guides recommend three directions with a rationale and limitations. Code-based material studies are labeled separately from photographic raster textures.

The checkout includes all assets needed for browsing, installation, export, and validation in `ramzes-backgrounds-1.1.0.tar.xz`. The unpacked source is cached under `.runtime/` and excluded from Git. Original PNG masters are retained in the separate full archival package and excluded from Git to keep downloads smaller. Rebuilding raster assets from source requires those masters and Pillow. Existing WebP assets work without rebuilding.

## Updates

```bash
git pull --ff-only
```

This updates the checkout. Installed skills are independent copies: back up or rename an existing skill folder before installing an updated copy. Existing client exports stay pinned by their lock files; updating the library does not change a deployed website.

## Validation and performance

```bash
python3 scripts/build_gallery.py
python3 scripts/validate.py
```

Validation requires Python with Pillow for image checks and Node.js for gallery JavaScript checks. It exercises all 500 standard exports, accent and neon variants, asset isolation, overwrite protection, token bindings, and metadata. This does not replace browser testing on the actual website.

Local query, export, and installation timings are recorded in [the benchmark report](docs/BENCHMARK.md). Agent selection and integration take longer than the file operations and depend on the model, project size, and verification needed.

## License and provenance

Original code, CSS, and SVG are provided under [MIT](LICENSE). Raster provenance is documented in [ASSET_ORIGINS.md](ASSET_ORIGINS.md). The code license does not relicense user-provided or generated source imagery.

No third-party component library is copied into this collection. Client websites receive only the selected static recipe and its required assets.

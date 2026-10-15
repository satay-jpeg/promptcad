# PromptCAD

A small, independent learning project that turns a constrained natural-language description into editable parametric OpenSCAD source. It is **not** a Meshy clone, a learned 3D model, or a general-purpose CAD system: it uses transparent rules and primitive geometry, with no external model/API, copied assets, weights, or Meshy branding.

## Try it

Requires Python 3.10+; no third-party packages.

```sh
python3 promptcad.py "box width 40 depth 20 height 8 mm" -o tray.scad
python3 promptcad.py "hollow cylinder radius 12 height 30 wall 2" -o sleeve.scad
python3 -m unittest -v
```

Open the `.scad` file in [OpenSCAD](https://openscad.org/) to preview, edit, and export mesh formats such as STL. OpenSCAD is optional; this tool only writes source files.

## Supported prompt patterns

- Box (default): `box width 40 depth 20 height 8`
- Sphere: `sphere radius 12`
- Hollow cylinder / tube / pipe / ring: `tube radius 12 height 30 wall 2`

Dimensions are millimetres by convention. Defaults are width=30, depth=20, height=10; sphere radius=10; cylinder radius=10, height=20, wall=2. This is a parser with keyword defaults, not semantic AI; unsupported requests fall back to a box. Inspect every generated dimension and shape.

## REA-assisted product investigation (public marketing page only)

REA is the independent, MIT-licensed reverse-engineering toolkit at [morluto/rea](https://github.com/morluto/rea). I built REA locally and used `inspect-web-page` against a separately launched Chrome page for Meshy's public text-to-3D feature page. REA returned structured evidence including the page title/URL, accessibility tree and page text; Evidence ID: `ev_7c327c391a82da24f13c2b55d9400f1648b7157938cc9ae93e0ef132d79063fc`. The evidence was filtered to the Meshy origin. The exact observation boundaries and source links are in [`research/rea-meshy-observation.md`](research/rea-meshy-observation.md).

From the page's claims and accessible public text, the visible workflow is describe an object → generate → inspect/iterate → download. The page advertises configurable generation, a viewer with wireframe/statistics/printability checks, refinement tools, and export formats. These are **product-page claims**, not independently verified behavior. The page does not disclose model architecture, training data, or internal generation algorithm; we did not inspect or access authenticated generation internals. REA was used for authorized, passive observation; no account, generation request, or private endpoint was accessed.

PromptCAD borrows only this high-level product workflow, not Meshy's implementation: prompt → deterministic shape/parameter parsing → editable OpenSCAD → user-side preview/refinement/export. Unlike a learned 3D model, it produces simple parameterized solids only. The architectural distinction is central: REA explains observable software behavior; it does not magically recover source or proprietary model internals.

## Legal / safety boundaries

This is an independent educational implementation from scratch. Do not copy proprietary source, model weights, datasets, UI, or brand assets; comply with licenses and terms for any dependencies, models, or reference material you add. This project makes no claim about Meshy's internal implementation and is not affiliated with Meshy or REA. MIT license applies to this repository's original code only. CAD output is an unvalidated draft: check dimensions, wall thickness, manifoldness, and suitability before fabrication; never use it for safety-critical parts.

## Next experiments

Add a proper grammar and explicit parameter schema; visualize geometry in a small web UI; add boolean operations and unit tests; optionally connect an openly licensed text-to-CAD model after reviewing its code, weights, data, and commercial-use terms.

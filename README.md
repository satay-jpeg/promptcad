# PromptCAD

A tiny, independent learning prototype that maps a limited natural-language prompt to editable parametric OpenSCAD source. It is **not** a Meshy clone, a learned 3D model, or a general-purpose CAD system: it uses transparent rules and primitive geometry, with no external model/API, copied assets, weights, or Meshy branding.

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

## How this relates to text-to-3D products

A commercial text-to-3D service typically combines a prompt interface, learned generative models that predict geometry (often mesh topology and surface appearance), post-processing/retopology, preview, and export. Its proprietary model architecture and training data are not disclosed by the product page, so this repo does not claim to reproduce them. Our intentionally simpler route is: prompt → keyword/dimension extraction → parametric OpenSCAD primitive → user opens/exports it. This makes the geometry understandable and editable, but much less expressive.

## Legal / safety boundaries

This is an independent educational implementation from scratch. Do not copy proprietary source, model weights, datasets, UI, or brand assets; comply with licenses and terms for any dependencies, models, or reference material you add. This project makes no claim about Meshy's internal implementation and is not affiliated with Meshy or REA. MIT license applies to this repository's original code only. CAD output is an unvalidated draft: check dimensions, wall thickness, manifoldness, and suitability before fabrication; never use it for safety-critical parts.

## Next experiments

Add a proper grammar and explicit parameter schema; visualize geometry in a small web UI; add boolean operations and unit tests; optionally connect an openly licensed text-to-CAD model after reviewing its code, weights, data, and commercial-use terms.

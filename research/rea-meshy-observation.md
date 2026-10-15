# REA observation notes: Meshy public text-to-3D page

**Observation type:** passive REA Chrome DevTools Protocol page inspection, not a reverse engineering of private service internals.

- Target: <https://www.meshy.ai/features/text-to-3d>
- REA project: <https://github.com/morluto/rea>, checked out from its public GitHub repository for local build/run.
- Exact invocation in the source checkout: `node scripts/rea.mjs inspect-web-page http://127.0.0.1:9229 C34C4BEA565E130A9F938223DBF1989C --observation-ms 1500 --include-accessibility-text --format json` (equivalent installed CLI form: `rea inspect-web-page …`).
- Evidence ID: `ev_7c327c391a82da24f13c2b55d9400f1648b7157938cc9ae93e0ef132d79063fc`
- REA captured the live page title/URL and accessibility tree (including the feature heading and page controls). The public feature page itself describes three stages—write a prompt, generate, download/use—and advertises model/type/pose/variation controls, viewer wireframe/statistics, refinement, printability checks, and multiple export formats. Those are product claims, not independently verified generation behavior.
- REA completeness reported `policy_filtered`; only the exact Meshy origin was allowed. The observation excluded third-party resources, script source, JSON body shapes, console text, storage values, WebSockets, and worker activity. No scripts were extracted or copied.
- Scope: public marketing page only. No sign-in, account creation, prompt submission, model generation, endpoint discovery, or access to Meshy's app internals was attempted. The inspection does not verify that advertised features behave as claimed or reveal how the generative model works.

## What we learned—and did not

We can describe the public user-facing workflow as prompt → generation → inspection/refinement → export. The page explicitly markets a generative 3D model and mesh-oriented options; it does not reveal model architecture, training data, internal representations, or service implementation. Those details remain unknown. REA provides evidence about observable software, not a means to reproduce an inaccessible proprietary model.

## Design consequences for PromptCAD

PromptCAD takes inspiration only from that generic staged workflow. It intentionally implements a different, inspectable technique: constrained text parsing produces deterministic parametric OpenSCAD code for a few primitive solids; a human can inspect and edit the source, then use OpenSCAD for viewing/export. No model training, hosted generation, Meshy/REA code, branding, or assets are included. This is an educational functional analogue, not equivalent output or capability.

## Sources

- REA README and public project documentation: <https://github.com/morluto/rea>
- REA website observation command reference: <https://github.com/morluto/rea/blob/main/docs/web-runtime.md>
- Meshy public text-to-3D feature page: <https://www.meshy.ai/features/text-to-3d>

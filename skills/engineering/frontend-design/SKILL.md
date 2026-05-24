---
name: frontend-design
description: Build distinctive, production-grade frontend interfaces with strong visual direction and polished interaction details. Use when the user asks to create or substantially redesign a web page, app screen, component, dashboard, game UI, or interactive frontend experience.
---

# Frontend Design

Use this skill when frontend work needs product design judgment, not just layout implementation. Treat it as a quality gate: "polished" never means generic decoration.

## Workflow

1. **Inspect first.** Read nearby pages, components, styles, tokens, screenshots, and design-system usage before choosing a direction.
2. **State the thesis.** Before editing, name the aesthetic direction, the audience/workflow it serves, and the memorable detail.
3. **Build the product.** The first screen should be usable UI, not marketing explanation, unless the user asked for a landing page.
4. **Verify visually.** When the project can run locally, inspect desktop and mobile viewports with a browser or screenshot workflow.

## Direction

Choose a specific direction grounded in the product: brutally minimal, editorial, industrial, playful, refined, dense/utilitarian, retro-futuristic, art deco, organic, maximalist, or another clear point of view. Do not choose "clean and modern" as the direction.

Make the interface feel like one designed object:

- Typography, color, spacing, motion, borders, shadows, icon style, and copy all support the same tone.
- Density matches purpose: operational tools are compact and scannable; editorial surfaces can breathe; games and playful tools can be more expressive.
- Component shapes feel related: radius, border weight, shadow depth, and control height are consistent.
- Copy sounds like one product across buttons, headings, empty states, and status text.

## Implementation

Build real working code in the project's existing framework and style.

Prefer:

- Existing components, tokens, routing, icons, and layout conventions
- Domain-specific UI over marketing-style filler
- Responsive layouts with stable dimensions and no text overlap
- Accessible contrast, keyboard behavior, and semantic structure
- Visual assets when they clarify the actual product, workflow, or data

Avoid:

- Card grids, centered hero-plus-feature sections, or landing pages unless requested
- Purple-blue gradients, decorative blobs, generic glass cards, and nested rounded panels
- Visible instructional text that explains the UI instead of making the UI clear
- New design systems or runtime dependencies without explicit user approval
- Animation that causes overlap, scroll jumps, unstable controls, or ignored reduced-motion preferences

## Typography And Motion

Treat type as a primary design material. Use the project's type scale and font stack when they exist; otherwise choose a font direction that matches the thesis, such as editorial serif, technical grotesk, compact utilitarian sans, display face, or monospace. Keep hierarchy readable at real UI density. Set line height, weight, and spacing deliberately; letter spacing should normally be `0`, not negative.

Use motion to clarify state, hierarchy, and interaction. Prefer CSS transitions/keyframes already supported by the stack. Add one coherent motion idea, such as staged entrance, spatial transition, hover feedback, drag feedback, progress, or live data change. Keep it fast enough for repeated product use and respect `prefers-reduced-motion`.

## Detail Pass

Before handoff, inspect the last 10%:

- Alignment: baselines, icon centering, control edges, grid columns, and section boundaries
- Spacing rhythm: related items closer together than unrelated items, with gaps from a visible scale
- Optical balance: large type, icons, charts, and empty areas balanced by eye
- Component fit: buttons, inputs, tabs, badges, and cards neither cramped nor inflated
- State craft: hover, focus, active, selected, disabled, loading, empty, and error states feel designed
- Edge content: long labels, empty lists, dense data, narrow screens, and high-contrast content still work
- Texture restraint: shadows, borders, gradients, blur, and transparency do not muddy readability

## Handoff

Report the design thesis, files changed, verification command, and any visual checks that could not be run.

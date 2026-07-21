
## 2026-07-21 - Accessible Responsive Buttons
**Learning:** When using responsive buttons where visible text is hidden on smaller screens (e.g., via Tailwind's `hidden lg:inline`), or for icon-only buttons, standard screen reader accessibility is lost. Additionally, the structural icon elements (like `<span class="material-symbols-outlined">`) can be read as raw ligatures.
**Action:** Always ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute and that the structural icon element has `aria-hidden="true"` applied to prevent screen readers from announcing raw ligatures.

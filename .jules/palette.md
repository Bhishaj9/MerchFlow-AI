
## 2026-06-28 - Explicit Accessible Names for Responsive Buttons
**Learning:** When interactive elements (like `<button>` or `<a>`) use responsive classes (e.g., `hidden lg:inline`) to conditionally hide text labels on smaller screens, they risk losing their accessible name on those viewports. Similarly, icon-only buttons rely entirely on inner elements (which might just be font ligatures read out loud).
**Action:** Always ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute if its visible text might be hidden via CSS. Furthermore, add `aria-hidden="true"` to structural icon elements (like `<span class="material-symbols-outlined">`) to prevent screen readers from reading raw ligatures.

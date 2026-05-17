
## 2024-05-18 - Responsive Button Text & Aria Labels
**Learning:** When visible text within an interactive element (`<button>` or `<a>`) is conditionally hidden using responsive viewport classes (e.g., `hidden lg:inline` via Tailwind), the element completely loses its accessible name for screen readers on smaller screens.
**Action:** Always provide an explicit `aria-label` attribute on the parent element to serve as a reliable fallback for screen readers across all viewports.

## 2024-05-18 - Material Symbols & Decorative SVGs
**Learning:** Structural icon elements like `<span class="material-symbols-outlined">` leak their raw ligatures (e.g. "rocket_launch" or "cloud_upload") to screen readers if not properly configured, causing auditory clutter.
**Action:** Always add `aria-hidden="true"` to icon spans to hide them from the accessibility tree. Crucially, before doing this, ensure the parent element (like the button) has a valid accessible name (such as visible text or an `aria-label`).

## 2026-02-28 - Accessible Responsive Buttons
**Learning:** Responsive buttons that hide their visible text on smaller viewports using Tailwind classes (like `hidden lg:inline`) become completely invisible to screen readers without an explicit ARIA label.
**Action:** Always provide an explicit `aria-label` attribute on parent interactive elements (`<button>` or `<a>`) when their visible text is conditionally hidden via CSS.

## 2026-02-28 - Material Symbols Accessibility
**Learning:** Material Symbols render using text ligatures (e.g., "rocket_launch", "arrow_back"). Screen readers will announce this literal ligature text unless it is explicitly hidden, which creates confusing announcements when combined with actual button text or aria-labels.
**Action:** Always apply `aria-hidden="true"` to structural icon elements (e.g., `<span class="material-symbols-outlined">`) when they are purely decorative or when their meaning is covered by the parent element's accessible name.

## 2024-05-24 - Responsive Icon-Only Button Accessibility
**Learning:** Hiding visible text on smaller viewports via responsive classes (e.g., `hidden lg:inline`) inadvertently creates icon-only interactive elements for those screen sizes, completely hiding them from screen readers if the icon uses raw ligatures without `aria-hidden="true"`.
**Action:** Always provide an explicit `aria-label` on the parent interactive element and `aria-hidden="true"` on the structural icon when using responsive hidden text, ensuring consistent accessible names across all viewport sizes.

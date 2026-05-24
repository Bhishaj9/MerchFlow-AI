## 2025-05-24 - Responsive Button Accessibility
**Learning:** When using responsive buttons where visible text is hidden on smaller screens via classes like `hidden lg:inline`, the parent interactive element loses its accessible name on those viewports.
**Action:** Ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` and any inner decorative icons have `aria-hidden="true"` to maintain consistent screen reader accessibility across all viewport sizes.

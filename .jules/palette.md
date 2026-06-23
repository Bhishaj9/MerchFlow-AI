## 2026-06-23 - Init

## 2026-06-23 - Responsive Button Accessibility
**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute to maintain consistent screen reader accessibility across all viewport sizes. Structural icon elements should include `aria-hidden="true"`.
**Action:** Always add descriptive `aria-label` attributes to responsive interactive elements and `aria-hidden="true"` to structural icons.

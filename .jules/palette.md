## 2026-07-16 - Responsive Accessibility Lost Context

**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), the element can lose its accessible name on those viewports if no `aria-label` is present. Furthermore, Material Symbol icons without `aria-hidden="true"` might cause screen readers to read raw ligatures if that's the only remaining text.
**Action:** Ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute and that decorative icons inside it use `aria-hidden="true"` to maintain consistent screen reader accessibility across all viewport sizes.

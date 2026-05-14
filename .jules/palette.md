## 2026-05-14 - Responsive Hidden Text and Accessible Names
**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), the element becomes effectively an icon-only element for mobile screen readers.
**Action:** Ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute to maintain consistent screen reader accessibility across all viewport sizes, and apply `aria-hidden="true"` to structural icon elements.

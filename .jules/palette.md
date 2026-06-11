
## 2026-06-11 - Responsive Button Accessibility
**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), ensuring the parent interactive element has an explicit `aria-label` attribute is critical to maintain consistent screen reader accessibility across all viewport sizes.
**Action:** Always add explicit `aria-label` attributes to interactive elements with responsive text visibility, and combine this with `aria-hidden="true"` on their child icon elements.

## 2025-02-18 - [Responsive Buttons ARIA Labels]
**Learning:** [When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), the parent interactive element (`<button>` or `<a>`) must have an explicit `aria-label` attribute to maintain consistent screen reader accessibility across all viewport sizes.]
**Action:** [Always ensure that buttons or links with responsive text display (`hidden md:inline`, `hidden lg:inline`, etc.) include an `aria-label` attribute.]

## 2024-05-24 - Accessibility improvements for icon-only buttons
**Learning:** Buttons or links with `hidden lg:inline` text classes lose their accessible names on small screens, causing screen readers to read nothing or raw icon ligatures.
**Action:** When creating responsive buttons/links that hide visible text on smaller screens, add an explicit `aria-label` attribute on the parent interactive element (`<button>` or `<a>`) to maintain consistent screen reader accessibility across all viewport sizes.

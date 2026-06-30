
## 2026-06-30 - Add ARIA Labels to Responsive and Icon-only Buttons
**Learning:** When using responsive buttons where visible text is hidden on smaller screens (`hidden lg:inline`), or for icon-only buttons, the interactive element must have an `aria-label` and the `material-symbols-outlined` span must have `aria-hidden="true"` to prevent screen readers from reading raw ligatures and ensure accessibility across all screen sizes.
**Action:** Always add `aria-label` to the parent interactive element and `aria-hidden="true"` to the inner material icon span.

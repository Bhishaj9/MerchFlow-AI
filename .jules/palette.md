## 2024-07-25 - Responsive Icon Buttons
**Learning:** When using responsive utility classes to hide text labels on smaller viewports (e.g., `hidden lg:inline`), the interactive element effectively becomes an icon-only button for those users.
**Action:** Always add an explicit `aria-label` to the parent `<button>` or `<a>` and `aria-hidden="true"` to the icon element whenever text is responsively hidden.

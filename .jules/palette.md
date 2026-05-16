## 2024-05-24 - Screen Reader Compatibility with Responsive Text & Material Symbols
**Learning:** When using responsive Tailwind classes like `hidden lg:inline` to hide text on smaller screens or `truncate`, or using icon-only buttons with `material-symbols-outlined`, screen readers either lose the accessible name entirely or read out the raw ligature text (e.g., "rocket_launch").
**Action:** Always add `aria-label` to the parent interactive element (`<button>` or `<a>`) and apply `aria-hidden="true"` to the inner icon `<span>` to ensure consistent accessibility across all screen sizes.

## 2024-05-24 - Screen Reader A11y for Responsive Tailwind Text
**Learning:** Buttons using Tailwind's `hidden lg:inline` for text labels lose their accessible name on smaller viewports when the text disappears, leaving only the icon. Additionally, Material Symbols ligatures are read aloud by screen readers if not hidden.
**Action:** Always add an explicit `aria-label` to the parent `<button>` or `<a>` when child text is responsively hidden, and strictly apply `aria-hidden="true"` to the icon `<span>`.

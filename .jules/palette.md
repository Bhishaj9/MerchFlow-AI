## 2026-02-23 - Accessible Icon-Only Responsive Buttons

**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute to maintain consistent screen reader accessibility across all viewport sizes. Furthermore, always hide the raw Material Symbols text ligatures from screen readers using `aria-hidden="true"`.

**Action:** Whenever creating a button or link that contains an icon (especially one styled via ligatures) and responsive text, proactively add an `aria-label` to the interactive element matching the intended action, and add `aria-hidden="true"` to the icon's `<span>`.

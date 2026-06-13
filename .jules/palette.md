## 2025-05-18 - Icon-Only Buttons Missing ARIA Labels

**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute to maintain consistent screen reader accessibility across all viewport sizes. Also, icon-only buttons need an `aria-label` attribute, and the icon elements inside them need `aria-hidden="true"`.

**Action:** Update the interactive elements to have `aria-label` and the inner icons to have `aria-hidden="true"`.

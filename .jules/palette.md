
## 2024-05-18 - [Add ARIA labels to responsive buttons and icons]
**Learning:** When text inside an interactive element like `<button>` or `<a>` is hidden on smaller screens using responsive utility classes (e.g., `hidden lg:inline` in Tailwind), the element can lose its accessible name for screen reader users on those breakpoints, especially if it only contains an icon otherwise.
**Action:** Always ensure that responsive buttons or links where text may be hidden have an explicit `aria-label` attribute on the parent interactive element. Also, add `aria-hidden="true"` to structural icon elements (like `<span class="material-symbols-outlined">`) to prevent screen readers from reading raw ligatures.

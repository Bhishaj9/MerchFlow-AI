## 2024-05-24 - Accessibility for responsive Material Symbols
**Learning:** When using responsive classes (like `hidden lg:inline`) on text within a button alongside an icon (like Material Symbols), the screen reader might not read anything on smaller screens if the text is hidden.
**Action:** Always ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute, and add `aria-hidden="true"` to the icon element (e.g. `<span class="material-symbols-outlined">`) to prevent screen readers from reading raw ligatures.


## 2024-06-10 - Adding `aria-label` to responsive interactive elements
**Learning:** When using responsive classes like `hidden lg:inline` on inner spans inside a `<button>` or `<a>` tag, the interactive element effectively becomes "icon-only" on smaller screens, hiding its accessible name from screen readers.
**Action:** Always provide an explicit `aria-label` attribute on the parent interactive element (`<button>` or `<a>`) to guarantee it maintains an accessible name regardless of the current viewport and responsive CSS states. Also, structural Material Symbols (`<span class="material-symbols-outlined">`) should have `aria-hidden="true"` if an `aria-label` is present on the parent, preventing the screen reader from reading raw ligatures.

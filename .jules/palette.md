## 2024-06-04 - Accessible Icons and Responsive Text
**Learning:** When using responsive buttons/links where visible text is hidden on small screens via Tailwind classes (e.g., `hidden lg:inline`), they lose accessible names on mobile. Also, structural icon elements (like `<span class="material-symbols-outlined">`) are read as raw ligatures by screen readers if not hidden.
**Action:** Ensure the parent interactive element has an explicit `aria-label` and the icon element has `aria-hidden="true"`.

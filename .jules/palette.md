## 2026-06-03 - Responsive Buttons and Icon Accessibility

**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (like `hidden lg:inline`), screen readers lose context. Additionally, structural icon elements (`material-symbols-outlined`) can be read out as meaningless ligatures if not hidden.

**Action:** Ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute to maintain consistent screen reader accessibility across all viewport sizes, and add `aria-hidden="true"` to nested icon spans.

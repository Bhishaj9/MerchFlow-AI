## 2023-11-23 - Initial Palette Journal
**Learning:** Accessibility and UX constraints for the project.
**Action:** Follow the boundaries.

## 2024-07-05 - Accessibility for Responsive and Icon-only Interactive Elements
**Learning:** When using responsive buttons or links where visible text is hidden on smaller screens via Tailwind classes (e.g., `hidden lg:inline`), or when using icon-only buttons, the parent interactive element (`<button>` or `<a>`) lacks an accessible name for screen readers. Furthermore, raw icon ligatures (like 'arrow_back' or 'content_copy') will be read aloud unless hidden.
**Action:** Ensure the parent interactive element (`<button>` or `<a>`) has an explicit `aria-label` attribute to maintain consistent screen reader accessibility across all viewport sizes. Additionally, strictly apply `aria-hidden="true"` to structural icon elements (like `<span class="material-symbols-outlined">`) to prevent screen readers from reading raw ligatures.

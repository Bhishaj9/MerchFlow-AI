## 2024-07-07 - Screen Reader Visibility vs Viewport Visibility
**Learning:** When using responsive utilities like Tailwind to hide visible text on smaller viewports (e.g., `hidden lg:inline`), or when using icon-only interactive elements (like Google Material Symbols which read as raw ligatures without `aria-hidden="true"`), screen reader users completely lose context.
**Action:** Always verify that interactive elements (`<button>`, `<a>`) have an explicit `aria-label` when their visible text could be hidden responsively, and always ensure structural icon spans have `aria-hidden="true"`.

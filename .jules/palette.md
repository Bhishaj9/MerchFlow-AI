## 2024-05-24 - Screen Reader A11y with Responsive Tailwind Utility Classes
**Learning:** When using responsive utility classes (like `hidden lg:inline`) to conditionally hide button text on smaller viewports, screen readers will lose the accessible name, leaving icon-only elements to be read as the raw ligature text (like "arrow_back").
**Action:** Always provide an explicit `aria-label` on interactive elements (`<button>`, `<a>`) where visible text might be hidden at certain breakpoints, and explicitly set `aria-hidden="true"` on the structural icon elements themselves.

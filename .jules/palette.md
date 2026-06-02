## 2026-06-02 - Accessible Names for Responsive Text Elements
**Learning:** Conditionally hiding text on small screens (e.g. `class="hidden lg:inline"`) removes the accessible name for interactive elements on smaller viewports, making them unreadable to screen readers.
**Action:** When hiding text using responsive classes, always add an explicit `aria-label` to the parent interactive element (`<button>`, `<a>`) and apply `aria-hidden="true"` to any accompanying icon fonts (e.g. Material Symbols) to prevent redundant or inaccurate readout.

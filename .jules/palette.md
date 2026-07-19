## 2024-05-24 - Responsive Text Accessibility
**Learning:** When using responsive utilities (e.g., `hidden lg:inline`) to hide text labels on smaller screens, interactive elements like buttons or links become inaccessible to screen readers because they lose their accessible name.
**Action:** Always add an explicit `aria-label` to the parent interactive element and `aria-hidden="true"` to its structural icons when visible text may be hidden via CSS.

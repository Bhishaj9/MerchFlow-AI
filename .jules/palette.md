## 2025-05-18 - ARIA Labels on Responsively Hidden Text
**Learning:** Text hidden via responsive classes like `hidden lg:inline` causes the parent interactive element to lack an accessible name on smaller screens, making it invisible to screen readers.
**Action:** Always add an explicit `aria-label` to the parent button/link when relying on CSS to hide its visible text.

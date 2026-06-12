## 2025-02-28 - Icon Button Accessibility
**Learning:** Using `title` tooltips alone on icon-only buttons (like Copy/Download) or relying on text hidden by responsive classes (like `hidden lg:inline`) is insufficient for robust accessibility across viewports.
**Action:** Always provide an explicit `aria-label` on the parent interactive element and `aria-hidden="true"` on the Material Symbol span to ensure clean screen reader announcements regardless of screen size.

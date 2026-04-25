
## 2026-03-01 - Material Symbols and Responsive Accessibility
**Learning:** In MerchFlow AI's glassmorphic UI, responsive text hiding (e.g., `hidden lg:inline` on the "Deploy" button) effectively turns standard buttons into icon-only buttons on small viewports. Furthermore, relying on Google Material Symbols ligatures without `aria-hidden="true"` causes screen readers to read the literal ligature text (e.g., "rocket_launch") aloud, confusing users.
**Action:** When buttons contain ligatures or decorative icons, always apply `aria-hidden="true"` to the icon element and add a descriptive `aria-label` to the parent `<button>` if the visible text is occasionally hidden or completely absent.

## 2024-06-27 - Icon Accessibility in Responsive Buttons
**Learning:** When text inside a button is hidden on small screens using Tailwind classes (like `hidden lg:inline`), the button loses its accessible name for screen reader users on mobile devices.
**Action:** Always add an explicit `aria-label` to buttons and links where visible text might be hidden responsively, and add `aria-hidden="true"` to decorative icons to prevent screen readers from reading raw icon font ligatures.

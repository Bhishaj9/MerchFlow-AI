## 2024-05-24 - [Accessible Icon Buttons]
**Learning:** Icon-only buttons using Material Symbols require both an `aria-label` on the `<button>` element and `aria-hidden="true"` on the `<span>` to prevent screen readers from reading the literal ligature text (like "rocket_launch").
**Action:** Always verify that every `<button>` or `<a>` tag containing only an icon has a descriptive `aria-label`, and the icon element itself (e.g. `<span>`) has `aria-hidden="true"`.

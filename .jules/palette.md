## 2024-03-24 - Material Symbols Aria Hidden
**Learning:** Structural icon elements like `<span class="material-symbols-outlined">` without `aria-hidden="true"` cause screen readers to read raw ligatures, resulting in poor accessibility.
**Action:** Always add `aria-hidden="true"` to purely decorative or structural icons (especially Material Symbols) to prevent screen reader noise, and ensure parent elements have appropriate accessible names via `aria-label` or text content.

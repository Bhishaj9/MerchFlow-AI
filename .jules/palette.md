## 2024-05-24 - Material Symbols Screen Reader Ligature Fix
**Learning:** Material Symbols use text ligatures (e.g., 'rocket_launch'). Without `aria-hidden="true"`, screen readers read the raw ligature text aloud, which severely degrades the experience for visually impaired users.
**Action:** Always add `aria-hidden="true"` to `<span class="material-symbols-outlined">` elements and ensure the interactive parent element (like a button or link) has a descriptive `aria-label` if it contains only the icon.

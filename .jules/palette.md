## 2024-04-09 - Accessible Material Icons
**Learning:** The app uses Google Material Symbols ligatures (e.g., `<span class="material-symbols-outlined">rocket_launch</span>`) for icons. Screen readers will erroneously announce the raw ligature text ("rocket launch") unless properly hidden, especially when the icon is part of a button or link.
**Action:** Always add `aria-hidden="true"` to `.material-symbols-outlined` span elements and rely on explicit `aria-label` attributes on the parent button/link to provide clear context for assistive technologies.

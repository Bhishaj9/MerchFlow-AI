## 2024-04-14 - Material Symbols Accessibility and Interactive Elements

**Learning:** When using text-ligature based icon libraries like Material Symbols (`<span class="material-symbols-outlined">...</span>`), the ligature text (e.g., "rocket_launch", "cloud_upload") is completely exposed to screen readers by default. This creates a confusing experience where users hear "rocket launch" instead of the intended semantic meaning of the element. Furthermore, icon-only interactive elements (like copy or download buttons) entirely lack accessible names, making them effectively invisible or unintuitive to assistive technologies.

**Action:**
1. Always apply `aria-hidden="true"` to structural icon elements (like `<span class="material-symbols-outlined">` and decorative SVGs) to hide the raw ligature text/graphic from screen readers.
2. For any interactive element (buttons, links) containing only an icon, ensure a descriptive `aria-label` is applied to the parent `<button>` or `<a>` tag to explicitly provide its semantic purpose.
3. Apply these rules uniformly across both static HTML and dynamic JS string injections.

## 2025-05-18 - Material Icons Need aria-hidden
**Learning:** Structural icon elements like `<span class="material-symbols-outlined">` and decorative SVG loading spinners are read aloud by screen readers if they contain text ligatures.
**Action:** Always add `aria-hidden="true"` to these elements to prevent confusing screen reader output. Added `aria-hidden="true"` to icon spans and inline SVGs across all HTML templates.

## 2025-05-18 - Icon-Only Buttons Need aria-label
**Learning:** Buttons like the "Copy JSON", "Download JSON", and "Deploy" buttons were missing accessible labels because they only contained icons.
**Action:** Added explicit `aria-label` attributes to these buttons (e.g., `id="copyBtn"`, `id="downloadBtn"`, `id="deployBtn"`) across all HTML files to ensure proper context for screen readers.

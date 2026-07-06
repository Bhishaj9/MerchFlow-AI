1. **Add ARIA Labels to Responsive Buttons/Links in `dashboard.html`**
   - The "Back to Home" link (`<a ... href="/">`) has its text hidden on smaller screens via `hidden lg:inline`, leaving only an icon visible. I need to add `aria-label="Back to Home"` to it.
   - The "Deploy" button (`<button id="deployBtn">`) has its text hidden on smaller screens via `hidden lg:inline`, leaving only an icon visible. I need to add `aria-label="Deploy"` to it.

2. **Add ARIA Labels to Responsive Buttons/Links in `glassui.html`**
   - The "Deploy" button (`<button id="deployBtn">`) has its text hidden on smaller screens via `hidden lg:inline`, leaving only an icon visible. I need to add `aria-label="Deploy"` to it.

3. **Ensure icon-only buttons have accessible names**
   - In `dashboard.html` and `glassui.html`, the "Copy JSON" and "Download JSON" buttons only have `title="..."` attributes and an icon. For better accessibility, they should have `aria-label`s since they only contain icons.
   - Add `aria-label="Copy JSON"` and `aria-label="Download JSON"` to those buttons.
   - Ensure the Material Symbols inside them have `aria-hidden="true"`.

4. **Add entry to `.jules/palette.md` journal**
   - Record the learning that buttons and links using Tailwind responsive classes (like `hidden lg:inline`) to hide their text on smaller screens must have explicit `aria-label` attributes to ensure consistent accessibility across breakpoints.

5. **Complete Pre-Commit Steps**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

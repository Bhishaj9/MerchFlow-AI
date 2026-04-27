1. **Add ARIA attributes to `dashboard.html` and `glassui.html`:**
   - Add `aria-label` to the "Back to Home", "Deploy", "Copy JSON", and "Download JSON" buttons/links, which either lack visible text entirely or hide it responsively on smaller viewports.
   - Add `aria-hidden="true"` to the corresponding `<span class="material-symbols-outlined">` elements to prevent screen readers from reading raw ligatures.
2. **Journaling:**
   - Create `.jules/palette.md` and add a new entry documenting the learning about handling Material Symbols and responsive hidden text for screen readers.
3. **Pre-commit Steps:**
   - Install testing dependencies and run the pytest suite (`python -m pytest test_*.py`) to ensure no regressions were introduced.
   - Run the pre commit tool to verify.
4. **Submit Change:**
   - Commit the changes and request user approval to push.

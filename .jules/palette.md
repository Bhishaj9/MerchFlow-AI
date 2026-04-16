
## 2026-04-16 - Prevent Screen Readers from Announcing Decorative Icon Ligatures
**Learning:** In codebases utilizing structural icon elements containing text ligatures (like `<span class="material-symbols-outlined">cloud_upload</span>`), screen readers will attempt to read the text ligature ("cloud_upload") out loud. This creates a confusing and non-intuitive experience for visually impaired users.
**Action:** When adding structural icon elements containing text ligatures, ensure that the element has `aria-hidden="true"` applied so screen readers ignore it. Additionally, ensure the associated button or interactable container has a descriptive `aria-label` to convey the intended action clearly.

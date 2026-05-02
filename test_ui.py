from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Navigate to the local dashboard.html
        url = "file:///app/dashboard.html"
        page.goto(url)

        # Verify the ARIA labels we added
        deploy_btn = page.locator("#deployBtn")
        assert deploy_btn.get_attribute("aria-label") == "Deploy", "Deploy button missing or wrong aria-label"

        back_link = page.locator("a[aria-label='Back to Home']")
        assert back_link.count() > 0, "Back to Home link missing aria-label"

        copy_btn = page.locator("#copyBtn")
        assert copy_btn.get_attribute("aria-label") == "Copy JSON", "Copy button missing or wrong aria-label"

        download_btn = page.locator("#downloadBtn")
        assert download_btn.get_attribute("aria-label") == "Download JSON", "Download button missing or wrong aria-label"

        # Verify aria-hidden on Material symbols within these elements
        assert deploy_btn.locator("span.material-symbols-outlined").get_attribute("aria-hidden") == "true", "Deploy button icon missing aria-hidden"
        assert copy_btn.locator("span.material-symbols-outlined").get_attribute("aria-hidden") == "true", "Copy button icon missing aria-hidden"
        assert download_btn.locator("span.material-symbols-outlined").get_attribute("aria-hidden") == "true", "Download button icon missing aria-hidden"

        print("✅ UI tests passed: ARIA labels and aria-hidden properties are correct.")
        browser.close()

if __name__ == "__main__":
    run()

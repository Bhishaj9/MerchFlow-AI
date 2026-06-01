from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('file:///app/dashboard.html')

        # Verify the presence of aria-labels
        assert page.locator('a[aria-label="Back to Home"]').count() > 0
        assert page.locator('button[aria-label="Deploy"]').count() > 0
        assert page.locator('button[aria-label="Copy JSON"]').count() > 0
        assert page.locator('button[aria-label="Download JSON"]').count() > 0

        # Take a screenshot
        os.makedirs('/home/jules/verification', exist_ok=True)
        page.screenshot(path='/home/jules/verification/a11y_fix.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    run()
    print("Verification passed and screenshot saved.")

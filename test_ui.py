from playwright.sync_api import sync_playwright
import os

def run_tests():
    os.makedirs('/home/jules/verification/screenshots', exist_ok=True)
    os.makedirs('/home/jules/verification/videos', exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(record_video_dir="/home/jules/verification/videos")
        page = context.new_page()

        page.goto("file:///app/dashboard.html")
        page.wait_for_selector("#deployBtn")

        # Verify the ARIA labels are accessible to the browser
        deploy_btn = page.locator("#deployBtn")
        print(f"Deploy Button aria-label: {deploy_btn.get_attribute('aria-label')}")

        copy_btn = page.locator("#copyBtn")
        print(f"Copy Button aria-label: {copy_btn.get_attribute('aria-label')}")

        page.screenshot(path="/home/jules/verification/screenshots/dashboard.png")

        context.close()
        browser.close()

if __name__ == "__main__":
    run_tests()

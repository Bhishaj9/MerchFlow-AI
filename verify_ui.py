from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:7860/dashboard")
    page.wait_for_timeout(1000)

    # Hover over buttons to ensure states render correctly and elements are accessible
    page.get_by_role("link", name="Back to Home").hover()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="Deploy").hover()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="Copy JSON").hover()
    page.wait_for_timeout(500)

    page.get_by_role("button", name="Download JSON").hover()
    page.wait_for_timeout(500)

    # Take screenshot at the key moment
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos",
            viewport={'width': 800, 'height': 600}
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()

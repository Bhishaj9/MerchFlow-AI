from playwright.sync_api import sync_playwright

def test_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Test dashboard.html
        page.goto("file:///app/dashboard.html")
        assert page.locator('a[aria-label="Back to Home"]').count() == 1
        assert page.locator('button[aria-label="Deploy"]').count() == 1
        assert page.locator('button[aria-label="Copy JSON"]').count() == 1
        assert page.locator('button[aria-label="Download JSON"]').count() == 1
        print("dashboard.html verified")

        # Test glassui.html
        page.goto("file:///app/glassui.html")
        assert page.locator('button[aria-label="Deploy"]').count() == 1
        assert page.locator('button[aria-label="Copy JSON"]').count() == 1
        assert page.locator('button[aria-label="Download JSON"]').count() == 1
        print("glassui.html verified")

        browser.close()

if __name__ == "__main__":
    test_ui()

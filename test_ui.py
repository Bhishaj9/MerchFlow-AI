from playwright.sync_api import sync_playwright

def test_dashboard_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('file:///app/dashboard.html')

        # Verify Deploy button aria-label
        deploy_btn = page.locator('#deployBtn')
        assert deploy_btn.get_attribute('aria-label') == 'Deploy'
        deploy_icon = deploy_btn.locator('span.material-symbols-outlined')
        assert deploy_icon.get_attribute('aria-hidden') == 'true'

        # Verify Back to Home link aria-label
        back_link = page.locator('a[href="/"]')
        assert back_link.get_attribute('aria-label') == 'Back to Home'
        back_icon = back_link.locator('span.material-symbols-outlined')
        assert back_icon.get_attribute('aria-hidden') == 'true'

        # Verify Copy JSON button aria-label
        copy_btn = page.locator('#copyBtn')
        assert copy_btn.get_attribute('aria-label') == 'Copy JSON'
        copy_icon = copy_btn.locator('span.material-symbols-outlined')
        assert copy_icon.get_attribute('aria-hidden') == 'true'

        # Verify Download JSON button aria-label
        download_btn = page.locator('#downloadBtn')
        assert download_btn.get_attribute('aria-label') == 'Download JSON'
        download_icon = download_btn.locator('span.material-symbols-outlined')
        assert download_icon.get_attribute('aria-hidden') == 'true'

        browser.close()

if __name__ == "__main__":
    test_dashboard_ui()
    print("UI Tests Passed!")

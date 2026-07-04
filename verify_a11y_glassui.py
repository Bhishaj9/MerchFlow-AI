from playwright.sync_api import sync_playwright

def verify_a11y_glassui():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('file:///app/glassui.html')

        # Check for Copy JSON button
        copy_btn = page.locator('button[id="copyBtn"]')
        assert copy_btn.get_attribute('aria-label') == 'Copy JSON', f"Expected aria-label 'Copy JSON', got '{copy_btn.get_attribute('aria-label')}'"
        copy_icon = copy_btn.locator('span[id="copyIcon"]')
        assert copy_icon.get_attribute('aria-hidden') == 'true', "Expected aria-hidden 'true' on copy icon"

        # Check for Download JSON button
        download_btn = page.locator('button[id="downloadBtn"]')
        assert download_btn.get_attribute('aria-label') == 'Download JSON', f"Expected aria-label 'Download JSON', got '{download_btn.get_attribute('aria-label')}'"
        download_icon = download_btn.locator('span:has-text("download")')
        assert download_icon.get_attribute('aria-hidden') == 'true', "Expected aria-hidden 'true' on download icon"

        # Check for Deploy button
        deploy_btn = page.locator('button[id="deployBtn"]')
        assert deploy_btn.get_attribute('aria-label') == 'Deploy', f"Expected aria-label 'Deploy', got '{deploy_btn.get_attribute('aria-label')}'"
        deploy_icon = deploy_btn.locator('span:has-text("rocket_launch")')
        assert deploy_icon.get_attribute('aria-hidden') == 'true', "Expected aria-hidden 'true' on deploy icon"

        print("Accessibility checks passed for glassui.html")
        browser.close()

if __name__ == '__main__':
    verify_a11y_glassui()
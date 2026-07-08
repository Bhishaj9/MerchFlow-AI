from playwright.sync_api import sync_playwright
import os

def run():
    os.makedirs('/home/jules/verification', exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Verify in a small viewport to trigger 'hidden sm:inline-flex' or similar mobile classes
        context = browser.new_context(viewport={'width': 400, 'height': 800})
        page = context.new_page()
        page.goto('file:///app/dashboard.html')
        page.wait_for_timeout(2000)
        page.screenshot(path='/home/jules/verification/dashboard_mobile.png')

        # Verify in a larger viewport
        context2 = browser.new_context(viewport={'width': 1200, 'height': 800})
        page2 = context2.new_page()
        page2.goto('file:///app/dashboard.html')
        page2.wait_for_timeout(2000)
        page2.screenshot(path='/home/jules/verification/dashboard_desktop.png')

        browser.close()

if __name__ == '__main__':
    run()

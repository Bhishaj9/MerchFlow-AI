import os
from playwright.sync_api import sync_playwright

def run():
    output_dir = "/home/jules/verification/screenshots"
    os.makedirs(output_dir, exist_ok=True)
    screenshot_path = os.path.join(output_dir, "dashboard.png")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("file:///app/dashboard.html", timeout=60000)
        page.screenshot(path=screenshot_path, full_page=True)
        browser.close()
        print(f"Screenshot saved to {screenshot_path}")

if __name__ == "__main__":
    run()

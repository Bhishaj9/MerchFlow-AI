from playwright.sync_api import sync_playwright
import os

def capture_screenshot(url, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=output_path)
        browser.close()

if __name__ == "__main__":
    os.makedirs("/home/jules/verification", exist_ok=True)
    capture_screenshot("file:///app/code.html", "/home/jules/verification/code_html.png")
    capture_screenshot("file:///app/dashboard.html", "/home/jules/verification/dashboard_html.png")
    capture_screenshot("file:///app/glassui.html", "/home/jules/verification/glassui_html.png")
    print("Screenshots captured successfully.")

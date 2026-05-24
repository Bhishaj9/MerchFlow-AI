from playwright.sync_api import sync_playwright
import os

def run():
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # View desktop
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto("file:///app/dashboard.html", timeout=30000)
        page.screenshot(path="/home/jules/verification/screenshots/dashboard_desktop.png")
        # View mobile to see responsive changes
        page.set_viewport_size({"width": 375, "height": 812})
        page.screenshot(path="/home/jules/verification/screenshots/dashboard_mobile.png")

        # Test glassui
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto("file:///app/glassui.html", timeout=30000)
        page.screenshot(path="/home/jules/verification/screenshots/glassui_desktop.png")

        browser.close()

if __name__ == "__main__":
    run()

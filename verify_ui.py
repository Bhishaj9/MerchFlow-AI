from playwright.sync_api import sync_playwright
import os

os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
os.makedirs("/home/jules/verification/videos", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(record_video_dir="/home/jules/verification/videos")
    page = context.new_page()

    page.goto("file:///app/dashboard.html", timeout=30000)
    page.screenshot(path="/home/jules/verification/screenshots/dashboard.png", full_page=True)

    page.goto("file:///app/glassui.html", timeout=30000)
    page.screenshot(path="/home/jules/verification/screenshots/glassui.png", full_page=True)

    context.close()
    browser.close()

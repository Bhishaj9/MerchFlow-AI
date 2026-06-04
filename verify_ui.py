from playwright.sync_api import sync_playwright
import os

os.makedirs('/home/jules/verification/', exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///app/dashboard.html')
    page.screenshot(path='/home/jules/verification/dashboard.png', full_page=True)
    page.goto('file:///app/glassui.html')
    page.screenshot(path='/home/jules/verification/glassui.png', full_page=True)
    browser.close()

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("file:///app/dashboard.html")
        await asyncio.sleep(2)  # Allow JS and CSS to initialize fully

        await page.screenshot(path="/home/jules/verification/dashboard_screenshot.png")

        # Test mobile viewport to ensure icons are still visible
        page = await browser.new_page(viewport={"width": 375, "height": 667})
        await page.goto("file:///app/dashboard.html")
        await asyncio.sleep(2)
        await page.screenshot(path="/home/jules/verification/dashboard_screenshot_mobile.png")

        await browser.close()
        print("Screenshots saved successfully.")

asyncio.run(main())

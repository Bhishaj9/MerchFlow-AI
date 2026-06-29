import asyncio
from playwright.async_api import async_playwright

async def verify_ui():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print("Testing dashboard.html...")
        await page.goto("file:///app/dashboard.html", timeout=60000)
        await page.screenshot(path="/home/jules/verification/dashboard_screenshot.png")

        print("Testing glassui.html...")
        await page.goto("file:///app/glassui.html", timeout=60000)
        await page.screenshot(path="/home/jules/verification/glassui_screenshot.png")

        print("Testing code.html...")
        await page.goto("file:///app/code.html", timeout=60000)
        await page.screenshot(path="/home/jules/verification/code_screenshot.png")

        await browser.close()
        print("Screenshots saved to /home/jules/verification/")

if __name__ == "__main__":
    asyncio.run(verify_ui())
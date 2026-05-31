import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("file:///app/dashboard.html", timeout=10000)
        await page.screenshot(path="/home/jules/verification/dashboard.png")
        await browser.close()

asyncio.run(main())

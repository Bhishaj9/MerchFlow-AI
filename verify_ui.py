import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto("file:///app/dashboard.html")
        await page.screenshot(path="/home/jules/verification/dashboard.png")

        await page.goto("file:///app/glassui.html")
        await page.screenshot(path="/home/jules/verification/glassui.png")

        await page.goto("file:///app/code.html")
        await page.screenshot(path="/home/jules/verification/code.png")

        await browser.close()

asyncio.run(main())

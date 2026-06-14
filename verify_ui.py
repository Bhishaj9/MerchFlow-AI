import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file:///app/dashboard.html", timeout=60000)
        await page.screenshot(path="/home/jules/verification/dashboard.png")

        await page.goto("file:///app/glassui.html", timeout=60000)
        await page.screenshot(path="/home/jules/verification/glassui.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

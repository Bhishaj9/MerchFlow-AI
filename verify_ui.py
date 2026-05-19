import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('file:///app/dashboard.html')
        await page.screenshot(path='/home/jules/verification/screenshots/dashboard_a11y.png', full_page=True)
        await browser.close()

asyncio.run(main())

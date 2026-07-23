import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('file:///app/dashboard.html', timeout=60000)

        # Save screenshot
        import os
        os.makedirs('/home/jules/verification/screenshots/', exist_ok=True)
        screenshot_path = '/home/jules/verification/screenshots/dashboard_a11y.png'
        await page.screenshot(path=screenshot_path)

        print(f"Screenshot saved to {screenshot_path}")
        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())

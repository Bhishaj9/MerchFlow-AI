import asyncio
import os
from playwright.async_api import async_playwright

async def verify_a11y():
    os.makedirs('/home/jules/verification/', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print("Testing dashboard.html...")
        await page.goto("file:///app/dashboard.html")
        await page.screenshot(path='/home/jules/verification/dashboard.png')

        print("Testing glassui.html...")
        await page.goto("file:///app/glassui.html")
        await page.screenshot(path='/home/jules/verification/glassui.png')

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_a11y())

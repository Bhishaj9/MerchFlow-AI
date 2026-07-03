import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    os.makedirs('/home/jules/verification', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('file:///app/dashboard.html', timeout=60000)
        await page.screenshot(path='/home/jules/verification/dashboard.png')
        await browser.close()

asyncio.run(run())

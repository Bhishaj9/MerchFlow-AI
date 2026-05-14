import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    os.makedirs('/home/jules/verification/screenshots', exist_ok=True)
    os.makedirs('/home/jules/verification/videos', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(record_video_dir='/home/jules/verification/videos')
        page = await context.new_page()
        await page.goto('file:///app/dashboard.html')
        await page.screenshot(path='/home/jules/verification/screenshots/dashboard.png', full_page=True)
        await context.close()
        await browser.close()

asyncio.run(run())

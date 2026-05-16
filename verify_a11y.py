import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(record_video_dir="/home/jules/verification/videos")

        os.makedirs("/home/jules/verification/screenshots", exist_ok=True)

        pages = [
            ("dashboard.html", "file:///app/dashboard.html"),
            ("glassui.html", "file:///app/glassui.html"),
            ("code.html", "file:///app/code.html")
        ]

        for name, url in pages:
            page = await context.new_page()
            await page.goto(url)
            await asyncio.sleep(2) # Give it some time to render
            await page.screenshot(path=f"/home/jules/verification/screenshots/{name}.png")
            print(f"Verified {name}")
            await page.close()

        await context.close()
        await browser.close()

asyncio.run(run())

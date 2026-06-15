import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    os.makedirs("/home/jules/verification", exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto("file:///app/dashboard.html")
        assert await page.locator("a[href='/']").get_attribute("aria-label") == "Back to Home"
        assert await page.locator("#deployBtn").get_attribute("aria-label") == "Deploy"
        assert await page.locator("#copyBtn").get_attribute("aria-label") == "Copy JSON"
        assert await page.locator("#downloadBtn").get_attribute("aria-label") == "Download JSON"
        await page.screenshot(path="/home/jules/verification/dashboard.png")

        await page.goto("file:///app/glassui.html")
        assert await page.locator("#deployBtn").get_attribute("aria-label") == "Deploy"
        assert await page.locator("#copyBtn").get_attribute("aria-label") == "Copy JSON"
        assert await page.locator("#downloadBtn").get_attribute("aria-label") == "Download JSON"
        await page.screenshot(path="/home/jules/verification/glassui.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
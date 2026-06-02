import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Navigate to the local dashboard.html
        await page.goto("file:///app/dashboard.html", wait_until="networkidle")

        # Wait a moment for any JS execution if needed
        await page.wait_for_timeout(2000)

        # Output the required screenshot for verification
        os.makedirs("/home/jules/verification", exist_ok=True)
        screenshot_path = "/home/jules/verification/a11y-dashboard.png"
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

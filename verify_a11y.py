import asyncio
from playwright.async_api import async_playwright

async def verify_a11y():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print("Testing dashboard.html...")
        await page.goto("file:///app/dashboard.html")

        # Test deploying button
        deploy_btn = page.locator('#deployBtn')
        print(f"Deploy Button aria-label: {await deploy_btn.get_attribute('aria-label')}")

        # Test copying JSON
        copy_btn = page.locator('#copyBtn')
        print(f"Copy Button aria-label: {await copy_btn.get_attribute('aria-label')}")

        # Test download JSON
        download_btn = page.locator('#downloadBtn')
        print(f"Download Button aria-label: {await download_btn.get_attribute('aria-label')}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_a11y())

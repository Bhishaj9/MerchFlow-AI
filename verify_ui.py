import asyncio
from playwright.async_api import async_playwright

async def verify_ui():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("file:///app/dashboard.html", timeout=60000)

        # Assert copyBtn
        copy_btn = page.locator("#copyBtn")
        await copy_btn.wait_for(state="attached")
        aria_label = await copy_btn.get_attribute("aria-label")
        assert aria_label == "Copy JSON output", f"copyBtn aria-label expected 'Copy JSON output', got {aria_label}"

        # Assert copyIcon
        copy_icon = page.locator("#copyIcon")
        await copy_icon.wait_for(state="attached")
        aria_hidden = await copy_icon.get_attribute("aria-hidden")
        assert aria_hidden == "true", f"copyIcon aria-hidden expected 'true', got {aria_hidden}"

        # Assert downloadBtn
        download_btn = page.locator("#downloadBtn")
        await download_btn.wait_for(state="attached")
        aria_label = await download_btn.get_attribute("aria-label")
        assert aria_label == "Download JSON output", f"downloadBtn aria-label expected 'Download JSON output', got {aria_label}"

        # Assert deployBtn
        deploy_btn = page.locator("#deployBtn")
        await deploy_btn.wait_for(state="attached")
        aria_label = await deploy_btn.get_attribute("aria-label")
        assert aria_label == "Deploy Catalog", f"deployBtn aria-label expected 'Deploy Catalog', got {aria_label}"

        # Take screenshot
        import os
        os.makedirs("/home/jules/verification", exist_ok=True)
        await page.screenshot(path="/home/jules/verification/dashboard_a11y.png", full_page=True)
        print("Verification completed successfully. Screenshot saved.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_ui())

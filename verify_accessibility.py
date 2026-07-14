import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Test default/large viewport (shows 'Deploy' text)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto("file:///app/dashboard.html", timeout=60000)

        print("Checking large viewport (1280x800)...")
        # Check Back to Home
        back_btn = page.locator("a[aria-label='Back to Home']")
        await back_btn.wait_for(state="attached")
        print("Back to Home aria-label present:", await back_btn.count() > 0)
        back_icon = back_btn.locator("span.material-symbols-outlined")
        print("Back to Home icon aria-hidden present:", await back_icon.get_attribute("aria-hidden") == "true")

        # Check Deploy
        deploy_btn = page.locator("button[aria-label='Deploy']")
        await deploy_btn.wait_for(state="attached")
        print("Deploy aria-label present:", await deploy_btn.count() > 0)
        deploy_icon = deploy_btn.locator("span.material-symbols-outlined")
        print("Deploy icon aria-hidden present:", await deploy_icon.get_attribute("aria-hidden") == "true")

        # Check Copy JSON
        copy_btn = page.locator("button[aria-label='Copy JSON']")
        await copy_btn.wait_for(state="attached")
        print("Copy JSON aria-label present:", await copy_btn.count() > 0)
        copy_icon = copy_btn.locator("span.material-symbols-outlined")
        print("Copy JSON icon aria-hidden present:", await copy_icon.get_attribute("aria-hidden") == "true")

        # Check Download JSON
        download_btn = page.locator("button[aria-label='Download JSON']")
        await download_btn.wait_for(state="attached")
        print("Download JSON aria-label present:", await download_btn.count() > 0)
        download_icon = download_btn.locator("span.material-symbols-outlined")
        print("Download JSON icon aria-hidden present:", await download_icon.get_attribute("aria-hidden") == "true")

        await page.screenshot(path="/home/jules/verification/dashboard_large.png")

        # Test mobile viewport (hides 'Deploy' text)
        page_mobile = await browser.new_page(viewport={"width": 375, "height": 667})
        await page_mobile.goto("file:///app/dashboard.html", timeout=60000)
        print("Checking mobile viewport (375x667)...")
        await page_mobile.screenshot(path="/home/jules/verification/dashboard_mobile.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

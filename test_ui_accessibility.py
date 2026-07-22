import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print("Testing dashboard.html...")
        await page.goto("file:///app/dashboard.html", timeout=10000)

        deploy_btn = page.locator("#deployBtn")
        await deploy_btn.wait_for(state="attached")
        aria_label = await deploy_btn.get_attribute("aria-label")
        print(f"Deploy button aria-label: {aria_label}")
        assert aria_label == "Deploy"

        # Test visually hidden icons
        rocket_icon = deploy_btn.locator(".material-symbols-outlined")
        aria_hidden = await rocket_icon.get_attribute("aria-hidden")
        print(f"Deploy button rocket icon aria-hidden: {aria_hidden}")
        assert aria_hidden == "true"

        await page.screenshot(path="/home/jules/verification/screenshots/dashboard_a11y.png")
        print("dashboard.html accessibility verified.")

        print("\nTesting glassui.html...")
        await page.goto("file:///app/glassui.html", timeout=10000)
        deploy_btn_glass = page.locator("#deployBtn")
        await deploy_btn_glass.wait_for(state="attached")
        assert await deploy_btn_glass.get_attribute("aria-label") == "Deploy"
        await page.screenshot(path="/home/jules/verification/screenshots/glassui_a11y.png")
        print("glassui.html accessibility verified.")

        print("\nTesting code.html...")
        await page.goto("file:///app/code.html", timeout=10000)
        deploy_btn_code = page.locator("button[aria-label='Deploy']")
        await deploy_btn_code.wait_for(state="attached")
        assert await deploy_btn_code.get_attribute("aria-label") == "Deploy"
        await page.screenshot(path="/home/jules/verification/screenshots/code_a11y.png")
        print("code.html accessibility verified.")

        await browser.close()
        print("\nAll accessibility tests passed successfully!")

asyncio.run(main())

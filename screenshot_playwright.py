from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Mock login user by bypassing the actual view login mechanics for simplicity, or fix auth
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://localhost:8000/")
        page.screenshot(path="index.png")

        browser.close()

if __name__ == "__main__":
    run()

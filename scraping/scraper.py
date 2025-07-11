from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_and_capture(url, screenshot_path="screenshots/chapter1.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path=screenshot_path)
        html_content = page.content()
        browser.close()

    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n")
    return text[:5000]
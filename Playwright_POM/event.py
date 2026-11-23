import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browsercontext():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://testautomationpractice.blogspot.com/")

        yield page

        browser.close()
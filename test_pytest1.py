from playwright.sync_api import sync_playwright, expect

import pytest
@pytest.mark.test
@pytest.mark.order
def test_locators3():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()      
    page = context.new_page()                
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_placeholder("Enter Name").fill("tripura")
    page.get_by_text("START").click()
    page.get_by_role("radio",name="Female").click()
    page.wait_for_timeout(3000)


def test_locators4():
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()      
    page = context.new_page()                
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_placeholder("Enter Name").fill("tripura")
    page.get_by_text("START").click()
    page.get_by_role("radio",name="Female").click()
    page.wait_for_timeout(3000)

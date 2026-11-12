
from playwright.sync_api import sync_playwright

def mouseevents():

  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.get_by_text("Point Me").hover()
      page.get_by_text("Copy Text").dblclick()
      page.get_by_text("Copy Text").click(button="right")
      page.locator('[id = "draggable"]').drag_to(page.locator('[id = "droppable"]'))
      #page.drag_and_drop('[id = "draggable"]','[id = "droppable"]')
    
mouseevents()

def alerts():

  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.get_by_placeholder("Enter Name").fill("tripura")
      page.wait_for_timeout(3000)

alerts()


def keyboardevents():

  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.get_by_placeholder("Enter Name").fill("tripura")
      page.keyboard.press("Control+A")
      page.keyboard.press("Control+C")
      page.keyboard.up("Tab")
      page.keyboard.down("Tab")
      #page.keyboard.press("Tab")
      page.keyboard.press("Control+V")
      page.wait_for_timeout(3000)

keyboardevents()


def ():

  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")

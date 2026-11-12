from playwright.sync_api import sync_playwright

#p = sync_playwright().start()
def browsercontext():
 with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")


    context2 = browser.new_context()
    page2 = context2.new_page()
    page3 = context2.new_page()
    page2.goto('https://www.amazon.in/')
    page.wait_for_timeout(3000)

    browsercontext()

#p.stop()


def browserNavigations():
  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.wait_for_timeout(3000)
      page.go_back()
      page.wait_for_timeout(3000)
      page.go_forward()
      page.wait_for_timeout(3000)
      page.reload()
      page.wait_for_timeout(3000)

browserNavigations()

def locators1():
  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.get_by_placeholder("Enter Name").fill("testing")
      page.get_by_text("START").click()
      page.get_by_role("radio",name="Female").click()
      page.wait_for_timeout(3000)
locators1()



def grabbingcontent():
  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.locator('#name').fill('prak')
      page.locator('#name').type('aena')
      page.locator('[value="female"]').click()
      page.locator('#country').select_option('india')
      page.locator('#colors').select_option(['blue','green'])
      page.wait_for_timeout(3000)
grabbingcontent()


def grabbingcontent1():
  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.locator('#name').fill('prak')
      page.locator('#name').type('aena')
      print(page.get_by_placeholder("Enter Name").get_attribute("id"))
      print(page.locator("button.start").text_content())
      print(page.locator("button.start").inner_text())
      print(page.locator("#name").input_value())
      print(page.locator('//table[@name="BookTable"]//tr[2]/td[2]').inner_text())
      print(page.locator('//table[@name="BookTable"]//tr[2]/td').count())

      page.wait_for_timeout(3000)
grabbingcontent1()


def mouseevents():

  with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      context = browser.new_context()
      page = context.new_page()
      page.goto("https://testautomationpractice.blogspot.com/")
      page.get_by_text("Point Me").hover()
      page.get_by_text("Copy Text").dblclick()
      page.get_by_text("Copy Text").click(button="right")
      page.locator('[id = "draggable"]').drop_to(page.locator('[id = "droppable"]'))
      page.drag_and_drop('[id = "draggable"]','[id = "droppable"]')

mouseevents()
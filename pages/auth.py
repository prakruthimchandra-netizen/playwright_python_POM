from playwright.sync_api import Page, expect

class Auth:

    def __init__(self, page):
        self.enterEmailtextBox = page.get_by_role("textbox",name="Enter mobile number or email")
        self.continueBtn = page.get_by_role("button",name="Continue")
        self.password = page.get_by_role("textbox", name="Password")
        self.signInBtn = page.get_by_role("button", name="Sign in")
        self.incorrectPw = page.get_by_text("your password is incorrect")

    def enterEmail(self):
        self.enterEmailtextBox.fill(
            "trainingplaywright@gmail.com"
        )

    def clickContinueBtn(self):
        self.continueBtn.click()

    def fillPw(self):
        self.password.fill("Welcome@04")

    def SignInBtn(self):
        self.signInBtn.click()

    def ValidateIncorrectPwMsg(self):
        expect(self.incorrectPw).to_be_visible()
from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page):
        self.accountsNdList = page.get_by_role("link", name="Hello, sign in Account & Lists")
        self.searchBoxTextbox = page.get_by_role("searchbox",name="Search Amazon.in")
        self.amazonLogo = page.get_by_role("link", name="Amazon.in")
        self.cartIcon = page.get_by_role("link", name="items in Cart")

    def clickOnAccountNdList(self):
        self.accountsNdList.click()

    def validateTheVisibilityOfSearchBox(self):
        expect(self.searchBoxTextbox).to_be_visible()
    def validateTheVisibilityOfAmazonLogo(self):
        expect(self.amazonLogo).to_be_visible()
    def validateTheVisibilityOfAddToCart(self):
        expect(self.cartIcon).to_be_visible()
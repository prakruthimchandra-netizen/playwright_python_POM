from playwright.sync_api import Page, expect

from pages.auth import Auth
from pages.home import HomePage


def test_validatePositiveLogin(page: Page, amazonNavigation):

    HomePageObj = HomePage(page)
    authObj = Auth(page)
    HomePageObj.clickOnAccountNdList()
    authObj.enterEmail("trainingplayright@gmail.com")
    authObj.clickOnContinueBtn()
    authObj.fillPW("Welcome@04")
    authObj.signInBtn()
    HomePageObj.validateTheVisibilityOfSearchBox()


def test_validateNegativeLogin(page: Page, amazonNavigation):

    HomePageObj = HomePage(page)
    authObj = Auth(page)
    HomePageObj.clickOnAccountAndLists()
    authObj.enterEmail("trainingplayright@gmail.com")
    authObj.clickContinueBtn()
    authObj.fillPW("yyyyy@4")
    authObj.signInBtn()
    authObj.validateIncorrectPwMsg()
from selenium.webdriver.common.by import By
from selene.support.shared import browser
from selene import by, be, have


def test_testsearchskill():
    browser.open("http://test.qahunter.ru/")
    browser.element(by.id("formInput#search")).type("Python")
    browser.element(".btn--lg").click()
    browser.element("/html/body/main/section[2]/div/div/div[1]/div/div/a[2]").should(have.text("Python"))

   
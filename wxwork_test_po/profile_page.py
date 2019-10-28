from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from wxwork_test_po.pages.contact_page import ContactPage


class ProfilePage(ContactPage):
    _update = (By.CSS_SELECTOR, "a[class='qui_btn ww_btn js_edit']")
    _disable = (By.CSS_SELECTOR, "a[class='qui_btn ww_btn js_disable']")
    _enable = (By.CSS_SELECTOR, "a[class='qui_btn ww_btn js_disable']")
    _confirm = (By.CSS_SELECTOR, "a[class='qui_btn ww_btn ww_btn_Blue']")


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def update(self):
        self.driver.find_element(*self._update).click()


    def enable(self):
        self.driver.find_element(*self._enable).click()

    def disable(self):
        self.driver.find_element(*self._disable).click()
        self.driver.find_element(*self._confirm).click()

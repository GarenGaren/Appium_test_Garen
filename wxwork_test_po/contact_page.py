from selenium.webdriver.common.by import By

from wxwork_test_po.base_page import base_page
from wxwork_test_po.profile_page import profile_page


class contact_page(base_page):
    def __init__(self, driver):
        self.driver = driver

    _click = (By.CSS_SELECTOR, ".js_add_member")
    _username = (By.CSS_SELECTOR, "input[id = 'username']")
    _id = (By.CSS_SELECTOR, "input[id = 'memberAdd_acctid']")
    _email = (By.CSS_SELECTOR, "input[id = 'memberAdd_mail']")
    _save = (By.CSS_SELECTOR, "a[class = 'qui_btn ww_btn js_btn_save']")
    _someone = (By.CSS_SELECTOR, "input[id='memberSearchInput']")

    def __init__(self, driver):
        self.driver = driver

    def test_add_people(self, username, id, email):
        str = "https:////work.weixin.qq.com/wework_admin/frame#contacts"
        self.driver.get(str)
        self.driver.find_elements(*self._click)[1].click()
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._id).send_keys(id)
        self.driver.find_element(*self._email).send_keys(email)
        self.driver.find_element(*self._save).click()

    def serch_someone(self, name):
        self.driver.find_element(*self._someone).send_keys(name)
        return profile_page(self.driver)

from selenium.webdriver.common.by import By

from wxwork_test_po.pages.profile_page import ProfilePage
from wxwork_test_po.pages.wxwork_page import WXworkPage


class ContactPage(WXworkPage):
    _click = (By.CSS_SELECTOR, ".js_add_member")
    _username = (By.CSS_SELECTOR, "input[id = 'username']")
    _id = (By.CSS_SELECTOR, "input[id = 'memberAdd_acctid']")
    _email = (By.CSS_SELECTOR, "input[id = 'memberAdd_mail']")
    _save = (By.CSS_SELECTOR, "a[class = 'qui_btn ww_btn js_btn_save']")
    _someone = (By.CSS_SELECTOR, "input[id='memberSearchInput']")

    def __init__(self, work):
        self.driver = work.driver


    def add_people(self, username, id, email):
        str = "https:////work.weixin.qq.com/wework_admin/frame#contacts"
        self.driver.get(str)
        self.driver.find_elements(*self._click)[1].click()
        self.driver.find_element(*self._username).send_keys(username)
        self.driver.find_element(*self._id).send_keys(id)
        self.driver.find_element(*self._email).send_keys(email)
        self.driver.find_element(*self._save).click()
        return self

    def serch_someone(self, name):
        self.driver.find_element(*self._someone).send_keys(name)
        return ProfilePage(self.driver)

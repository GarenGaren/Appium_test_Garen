from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from wxwork_test_po.pages.profile_page import ProfilePage


class ManagementToolsPage(ProfilePage):

    _update = (By.CSS_SELECTOR, "div[class='manageTools_cnt_item_desc_title']")
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def go_to_photo(self):
        self.driver.find_element(*self._update).click()
        return
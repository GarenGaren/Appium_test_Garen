from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from wxwork_test_po.pages.wxwork_page import wxwork_page


class management_tools_page(wxwork_page):

    _update = (By.CSS_SELECTOR, "div[class='manageTools_cnt_item_desc_title']")
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def go_to_photo(self):
        self.driver.find_element(*self._update).click()
        return
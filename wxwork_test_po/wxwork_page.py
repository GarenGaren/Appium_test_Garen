from selenium.webdriver.common.by import By

from wxwork_test_po.base_page import base_page
from wxwork_test_po.contact_page import contact_page


class wxwork_page(base_page):
    def __init__(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def pass1(self):
        pass

    def go_to_contact_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[id='menu_contacts']").click()
        return contact_page(self.driver)

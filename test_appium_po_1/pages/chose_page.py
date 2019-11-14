from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium_po_1.pages.search_page import SearchPage


class ChosePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def go_to_search(self):
        self.driver.find_element_by_id("action_search")
        return SearchPage(self.driver)


    def delete(self,key):
        el1=self.driver.find_element_by_xpath("//*[@text='"+key+"']")
        TouchAction(self.driver).long_press(el=el1, duration=3000).release().perform()
        self.driver.find_element_by_xpath("//*[@text='删除']").click()

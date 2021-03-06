import logging
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_appium_po_1.pages.chose_page import ChosePage
from test_appium_po_1.pages.search_page import SearchPage


class MainPage():
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        self.actions = TouchAction(self.driver)
        # self.driver.find_element_by_id("image_cancel").click()

    def go_to_search(self):
        self.driver.find_element_by_id("tv_search").click()
        # self.driver.find_element_by_id("name").click()
        return SearchPage(self.driver)
    #显示等待 某个元素出现
    def show_wait_find_element(self, *loc):
        try:
            return WebDriverWait(self.driver, 10).until(expected_conditions .visibility_of_element_located(*loc))
        except Exception as msg:
            logging.info(msg)
            return None

    def go_to_chose_page(self):
        self.driver.find_element_by_xpath("//*[@text='自选']").click()
        return ChosePage(self.driver)

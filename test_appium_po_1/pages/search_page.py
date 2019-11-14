import time

from selenium.webdriver.remote.webdriver import WebDriver


class SearchPage():
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, key):
        self.driver.find_element_by_xpath("//*[@text='" + key + "']").click()
        # self.driver.find_element_by_id("name").click()

    def add(self, ):
        el1 = self.driver.find_elements_by_xpath(
            "//*[@resource-id='com.xueqiu.android:id/floating_action_image_view_id'] /../android.widget.TextView")[3]
        if el1.text == "加自选":
            el1.click()
        else:
            return el1.text
        return el1.text

    # def add_again(self):
    #     el1 = self.driver.find_elements_by_xpath("//*[@text='加自选']")[0]

    def cancel(self, key):
        self.driver.find_elements_by_xpath(" //*[@text='已添加']")[0].click()

    def quit_searcg_page(self):
        self.driver.find_element_by_id("action_close").click()

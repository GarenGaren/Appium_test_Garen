from selenium.webdriver.remote import webdriver


class base_page():

    def __init__(self):
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(50)

    def click_by_js(self, by, locator):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, locator))


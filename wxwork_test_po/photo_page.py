from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wxwork_test_po.wxwork_page import wxwork_page


class photo_page(wxwork_page):

    def __init__(self, driver: WebDriver):
        self.driver = driver
    def test_wxwork_upload_file(self):
        self.driver.find_element(By.CSS_SELECTOR, "span[class='ww_commonImg ww_commonImg_AddMember'").click()
        # elemente_upload = self.driver.find_element(By.CSS_SELECTOR, "input[id = 'js_upload_input']")
        # self.driver.execute_script("arguments[0].click();", elemente_upload)
        """绕过系统输入，直接通过input输入文件路径"""
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'js_upload_input']").send_keys("C:\\Users\\Administrator\\Desktop\\timg.jpg")
        """显示等待,直到某个元素在dom树中不可见, method方法返回为true.程序继续执行"""
        WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element_located(self.driver.find_element(By.CSS_SELECTOR,"a[id='ccc']")))

        self.driver.find_element(By.CSS_SELECTOR,"a[d_ck='submit']").click()
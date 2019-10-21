import time

from selenium.webdriver.common.by import By

from wxwork_test_po.pages.base_page import base_page
from wxwork_test_po.pages.contact_page import contact_page


class wxwork_page(base_page):
    def __init__(self):
        str = 'https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu'

        cookie = {
            "wwrtx.i18n_lan": "zh",
            "wwrtx.ref": "direct",
            "wwrtx.refid": "302078651253547",
            "wwrtx.d2st": "a5545690",
            "wwrtx.sid": "7KA9s8hAVXE1pxpSEHGCRCp5sALSO2RS5YsTCSX7ah4S5GY5NID2smgVeqFRKoh4",
            "wwrtx.ltype":"1",
            "wxpay.corpid":"1970325076090726",
            "wxpay.vid": "1688854031826396",
            "wwrtx.vst": "IPlXZY0sBGqQrPDsJ7Z25S5LG8D6jQjmwaVxuhHH9iuZrSSCmTvEr7oqGbyDzYLLv-RDQkLH5YE29UkuO_p9LLhAYlFuEzmCi6fxI69py5MtIgy86r7T4q4GbHMKlrGQmGF9X-8ogfPDgMHBWjtx-u1Arsoizcw9j9TeROXN1N5SxoVOKZjQdX3myWe5twkbn8BDPespTE4Lh_S3I9ULJB9sDCfkcMpmiJq74ig3gX9Y-wGJQv9esk9ug9avA3BQK8qQZvwTmJfy1TvE6aNk4g",
            "wwrtx.logined": "1"

        }
        self.driver.get(str)
        time.sleep(5)
        '''添加cookie'''
        for k,v in cookie.items():
            self.driver.add_cookie({"name":k,"value":v})
        self.driver.get(str)

    def quit(self):
        self.driver.quit()

    def go_to_contact_page(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[id='menu_contacts']").click()
        return contact_page(self.driver)

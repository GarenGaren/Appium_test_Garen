import time

from selenium.webdriver.common.by import By


from wxwork_test_po.pages.contact_page import ContactPage


class WXworkPage():
    def __init__(self):
        str = 'https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu'

        cookie = {
            "wwrtx.i18n_lan": "zh",
            "wwrtx.ref": "direct",
            "wwrtx.refid": "302078651593677",
            "wwrtx.d2st": "a7914693",
            "wwrtx.sid": "7KA9s8hAVXE1pxpSEHGCRIH1WXEH11DEx-26EmH3UG59-GUAZEr-Aoj_KoIGnDOB",
            "wwrtx.ltype":"1",
            "wxpay.corpid":"1970325076090726",
            "wxpay.vid": "1688854031826396",
            "wwrtx.vst": "N0ecMm4G0EVzEq9beV5zO1KhcGktrNeWSP8Vx5cR7v1yDbO5EQcXpMUyg6SemQyK2T6cuI289QAo2E-TsolG1NS65xALVpZLHUcAleya4YjCwfzU1Lg91nxrDnrPlCXTTKbRpPS85KhS2ImEbzh_OGQpLekFsK1Xly8fyjOECde4GgmihsbUm_24dcYyg9cWgqcSyKE6__49AeqCS9FSUyDl3fJH92ojyVs20rC_9JuqZ5nGKvjMysaV86h35zKUWTpLUcUW73zfbLao2AmUBA",
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
        return ContactPage(self.driver)

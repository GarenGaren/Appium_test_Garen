#! user/bin/env python3
# -*- coding:utf-8 -*-
import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_Selenium():

    def setup_method(self):
        """
        使用CMD命令打开chrome的远程调试
        :return:
        """
        # cmd = "chrome.exe --remote-debugging-port=9222"
        # os.popen(cmd)
        # time.sleep(3)
        # options = webdriver.ChromeOptions();
        # options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(chrome_options=options);
        self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(50)
        # self.driver.get("https://testerhome.com/")

    def teardown_method(self):
        time.sleep(1115)
        self.driver.quit();

    def test_wxwork_upload_file(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#material/image")
        self.driver.find_element(By.CSS_SELECTOR, "span[class='ww_commonImg ww_commonImg_AddMember'").click()
        # elemente_upload = self.driver.find_element(By.CSS_SELECTOR, "input[id = 'js_upload_input']")
        # self.driver.execute_script("arguments[0].click();", elemente_upload)
        """绕过系统输入，直接通过input输入文件路径"""
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'js_upload_input']").send_keys(
            "C:\\Users\\Administrator\\Desktop\\timg.jpg")
        """显示等待,直到某个元素在dom树中不可见, method方法返回为true.程序继续执行"""
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(
            self.driver.find_element(By.CSS_SELECTOR, "a[id='ccc']")))
        self.driver.find_element(By.CSS_SELECTOR, "a[d_ck='submit']").click()

    def test_add_people(self):
        str = "https:////work.weixin.qq.com/wework_admin/frame#contacts"
        self.driver.get(str)
        self.driver.find_elements(By.CSS_SELECTOR, ".js_add_member")[1].click()
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'username']").send_keys("richManager")
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'memberAdd_acctid']").send_keys("richManager")
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'memberAdd_mail']").send_keys("12315464@qq.com")
        self.driver.find_element(By.CSS_SELECTOR, "a[class = 'qui_btn ww_btn js_btn_save']").click()

    def test_cookie(self):
        """
        利用添加cookie的方式,绕过登陆.通过F12查看登陆前得cookie,然后登陆后查看已登陆的cookie,将这些cookie信息记录下来与登陆前cooie进行对比,将有差异的cookie添加到请求中
        :return:
        """
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
        time.sleep(2)
        '''添加cookie'''
        for k,v in cookie.items():
            self.driver.add_cookie({"name":k,"value":v})
        self.driver.get(str)
        time.sleep(20)

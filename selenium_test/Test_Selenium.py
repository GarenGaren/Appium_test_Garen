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
        options = webdriver.ChromeOptions();
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(chrome_options=options);
        # self.driver = webdriver.Chrome();
        self.driver.implicitly_wait(50)
        # self.driver.get("https://testerhome.com/")

    def teardown_method(self):
        time.sleep(1115)
        self.driver.quit();

    def test_KeyWord(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "div button[data-toggle='dropdown'] i[class='fa fa-list']")
        self.driver.execute_script("arguments[0].click();", element)
        print(
            self.driver.find_element(By.CSS_SELECTOR, "div button[data-toggle='dropdown'] i[class='fa fa-list']").text)
        time.sleep(5);
        self.driver.find_element(By.CSS_SELECTOR, "li a[href='#%E5%A5%96%E5%93%81%E9%A2%84%E8%A7%88']").click()
        print(
            self.driver.find_element(By.CSS_SELECTOR, "li a[href='#%E5%A5%96%E5%93%81%E9%A2%84%E8%A7%88']").text)
        time.sleep(10);

    def test_least_pulish(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/topics']").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/topics/last']").click()
        assert "急聘测试开发工程师" in self.driver.page_source

    def test_hogwarts(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[title='霍格沃兹测试学院']").click()
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "a[title='十期测试开发系列进阶课程-汇总贴']").click()
        str = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-danger']").text
        assert "访问被拒绝，你可能没有权限或未登录。" in str

    def test_login_with_error_keyword(self):
        self.test_hogwarts()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("12345")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        str = self.driver.find_element(By.CSS_SELECTOR, "div[class='alert alert-warning']").text
        assert "帐号或密码错误。" in str

    def test_testwomen(self):
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, "input[class='form-control']").send_keys("测试媛")
        self.driver.find_element(By.CSS_SELECTOR, "input[class='form-control']").send_keys(Keys.ENTER)
        str = self.driver.find_element(By.CSS_SELECTOR, "a[href='/topics/4331']").text
        print(str)
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/topics/4331']").click()
        str2 = self.driver.find_element(By.CSS_SELECTOR, "div h1>a+span[class='title']").text
        assert str == str2

    def test_wxwork_upload_file(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#material/image")
        self.driver.find_element(By.CSS_SELECTOR, "span[class='ww_commonImg ww_commonImg_AddMember'").click()
        # elemente_upload = self.driver.find_element(By.CSS_SELECTOR, "input[id = 'js_upload_input']")
        # self.driver.execute_script("arguments[0].click();", elemente_upload)
        """绕过系统输入，直接通过input输入文件路径"""
        self.driver.find_element(By.CSS_SELECTOR, "input[id = 'js_upload_input']").send_keys("C:\\Users\\Administrator\\Desktop\\timg.jpg")
        """显示等待,直到某个元素在dom树中不可见, method方法返回为true.程序继续执行"""
        WebDriverWait(self.driver,10).until(expected_conditions.invisibility_of_element_located(self.driver.find_element(By.CSS_SELECTOR,"a[id='ccc']")))

        self.driver.find_element(By.CSS_SELECTOR,"a[d_ck='submit']").click()
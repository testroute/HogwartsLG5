# Generated by Selenium IDE
import json,pytest
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# d = webdriver.Chrome()
# d.get("https://work.weixin.qq.com/wework_admin/frame#index")

class Testweixin():
    def setup_method(self):
        print("参数设置")
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        print("设置完成")
    # def teardown_method(self):
    #     self.driver.quit()
    def test_getcookie(self):
        cookies = self.driver.get_cookies()
        # 以文件流的形式打开文件
        with open("cookie.json", "w") as f:
        # 存储 cookie 到 cookie.json
            json.dump(cookies, f)
        f.close()
    def test_cookie(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        print("get cookies")

        # 以文件流的形式打开文件
        with open("cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
        f.close()
        print("got cookies")

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def test_testweixin(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]').click()
    def teardown_method(self):
        self.driver.quit()
if __name__=="__main__":
    path = os.path.dirname(__file__).__add__("\\selenium_work.py")
    pytest.main([path])
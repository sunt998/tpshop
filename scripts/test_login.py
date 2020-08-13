import os, sys
import time
sys.path.append(os.getcwd())
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page.login_page import LoginPage
from base.base_driver import init_driver
from base.base_yml import yml_data_with_file
class TestLogin:

    def setup(self):
        self.driver=init_driver()
        self.login_page = LoginPage(self.driver)

    @pytest.mark.parametrize("args", yml_data_with_file("login_data",'test_login'))
    def test_login(self, args):
        self.login_page.input_username(args['username'])
        self.login_page.input_password(args['password'])
        self.login_page.click_login()
        time.sleep(5)
        self.login_page.screenshot(args['screen'])
        # 成功就向下执行
        print(self.login_page.is_errorTip())
        if self.login_page.is_errorTip():
            # 登录成功后返回我的主页
            self.driver.keyevent(4)
            # 点击设置页面，再退出
            self.login_page.click_set()
            # 找到退出按钮并点击
            self.login_page.click_back()

        assert self.login_page.is_errorTip()

    def teardown(self):
        print("测试结束hahaha")
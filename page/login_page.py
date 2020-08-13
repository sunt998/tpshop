import os, sys
from selenium.webdriver.common.by import By
sys.path.append(os.getcwd())
import time
from base.base_action import BaseAction
class LoginPage(BaseAction):
    # 我的
    mine_button = By.XPATH, "//*[contains(@text,'我的')]"
    # 登录/注册
    loginRegist_button = By.XPATH, "//*[contains(@text,'登录/注册')]"
    # 用账号密码登录
    accoun_button = By.ID, "com.xiaomi.shop:id/entry_to_password_login"
    # 用户名
    username_btn = By.ID,'com.xiaomi.shop:id/et_account_name'
    # 密码
    pwd_btn = By.ID,'com.xiaomi.shop:id/et_account_password'
    # 登录
    login_btn = By.ID,"com.xiaomi.shop:id/btn_login"
    # 错误提示文字 用户名密码不匹配
    error_btn = By.ID,'com.xiaomi.shop:id/error_password_tips'
    # 设置按钮
    set_btn = By.ID,'com.xiaomi.shop.plugin.homepage:id/mine_root_icon_setting'
    # 退出按钮
    back_btn =By.ID,'com.xiaomi.shop2.plugin.setting:id/common_button_rootview'


    def __init__(self, driver):
        BaseAction.__init__(self,driver)
        # 前置代码，调到账号、密码登录界面
        self.jump_to_login()

     #4 输入用户名
    def input_username(self,text):
        self.input_text(self.username_btn,text)

    #5 输入密码
    def input_password(self,text):
        self.input_text(self.pwd_btn,text)

    #6 点击登录
    def click_login(self):
        self.click(self.login_btn)

    #7 判断是否登录
    def is_errorTip(self):
        try:
            ele = self.driver.find_element(self.error_btn[0],self.error_btn[1])
            # print(ele.text)
            return False
        except Exception:
            return True

    # 登录成功需要退出
    # 8 点击登录成功后的设置页面
    def click_set(self):
        self.click(self.set_btn)
    # 9 模拟手势的下滑操作,找到退出按钮并点击
    def click_back(self):
        self.driver.swipe(50,1583,50,463,3000)
        # 10 点击退出账号
        self.click(self.back_btn)
        # 11 用绝对坐标点击退出由于焦点问题,只能用坐标定位
        time.sleep(3)
        self.driver.tap([(780, 2010)])
    def jump_to_login(self):
        # 1 点击我的
        self.click(self.mine_button)
        # 2 点击登录注册
        self.click(self.loginRegist_button)
        # 3 点击用账号密码登录
        self.click(self.accoun_button)



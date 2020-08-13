import os,sys
sys.path.append(os.getcwd())
from appium import webdriver
def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = 'com.xiaomi.shop'
    desired_caps['appActivity'] = 'com.xiaomi.shop2.activity.MainActivity'
    # 解决输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] = True  # 保留软件数据,否则每次一开始都要有一些权限问题,会报错的
    # 声明我们的driver对象
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver
// 在Appium中用的Selenimu造的轮子
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click(self,loc):
        ele = WebDriverWait(self.driver, 5.0, 1.0).until(lambda x: x.find_element(loc[0], loc[1]))
        ele.click()

    def input_text(self,loc,text):
        ele = WebDriverWait(self.driver, 5.0, 1.0).until(lambda x: x.find_element(loc[0], loc[1]))
        ele.send_keys(text)

    def screenshot(self,filename):
        self.driver.get_screenshot_as_file("./screen/"+filename+".png")


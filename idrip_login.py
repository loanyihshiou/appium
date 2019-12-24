from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class IdripLogin:

    def __init__(self, idrip):
        self.idrip = idrip

    def login(self, username, password):
        """登入"""
        self.idrip.find_element_by_id("com.coffee.iDrip:id/linearLayout_my").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/textView_name").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/textview_login").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/editText_email").send_keys(username)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/editText_pw").send_keys(password)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/linearLayout_next").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/textview_skip").click()


if __name__ == "__main__":
    print("only this page")
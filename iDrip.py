# -*- coding: UTF-8 -*-
from appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import os
from Idrip_login import IdripLogin


class IdripTest(unittest.TestCase):

    def setUp(self):
        os.system("adb install /Users/yihshiou/PycharmProjects/Appium/apk/com.coffee.iDrip.apk")
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.0',
            'deviceName': 'QYJ7N17907000216',
            # 'deviceName': 'Android emulator',
            'automationName': 'uiautomator2',
            'appPackage': 'com.coffee.iDrip',
            'appActivity': 'com.project.baseproject.activity.main.Start_Activity'}
        self.idrip = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.idrip.implicitly_wait(10)
        """同意權限"""
        self.idrip.find_element(By.ID, "com.coffee.iDrip:id/textView_yes").click()
        time.sleep(1)
        self.idrip.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.idrip.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        self.idrip.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

    def tearDown(self):
        self.idrip.quit()
        os.system("adb uninstall com.coffee.iDrip")

    # @unittest.skip
    def test01_shopping_cart(self):
        idrip = IdripLogin()
        idrip.login("louistest0625@gmail.com", 711228)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/view_salon").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/asyncImageGlideView").click()
        # 下滑三次
        for i in range(3):
            self.swipe_up(1000)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/view_add").click()
        time.sleep(2)
        for i in range(2):
            self.idrip.find_element_by_id("com.coffee.iDrip:id/view_add").click()
            time.sleep(1)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/button_ok").click()
        time.sleep(0.5)
        toast = IdripLogin.is_toast_exist("加入購物車完成")
        self.assertEqual(toast, True)

    # @unittest.skip
    def test02_market(self):
        idrip = IdripLogin()
        idrip.login("louistest0625@gmail.com", 711228)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/linearLayout_shop").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/textView_subtitle").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/button").click()
        self.idrip.find_element_by_xpath("//android.widget.TextView[@text='香檳金']").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/view_add").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/button_ok").click()
        time.sleep(0.5)
        toast = self.is_toast_exist("購物車完成")
        self.assertEqual(toast, True)

    # @unittest.skip
    def test03_market(self):
        self.login("louistest0625@gmail.com", 711228)
        self.idrip.find_element_by_xpath("//android.widget.TextView[@text='咖啡市集']").click()
        self.idrip.find_element_by_xpath(
            "//android.widget.TextView[contains(@resource-id, 'packet') and @text='咖啡包']").click()
        self.swipe_up(500)
        self.idrip.find_element_by_xpath("//android.widget.RelativeLayout[@index='2']").click()
        self.idrip.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                         "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                         ".FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android"
                                         ".widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget"
                                         ".RelativeLayout[2]/android.view.View[1]").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/button_ok").click()
        toast = self.is_toast_exist("加入購物車完成")
        self.assertEqual(toast, True)


if __name__ == '__main__':
    unittest.main(verbosity=2)


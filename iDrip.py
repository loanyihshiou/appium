# -*- coding: UTF-8 -*-
from appium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest
import os
from IdripBase import IdripMethod


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
            'appActivity': 'com.coffee.idrip.MainActivity'
        }
        self.idrip = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.idrip.implicitly_wait(10)

    def tearDown(self):
        self.idrip.quit()
        os.system("adb uninstall com.coffee.iDrip")

    # @unittest.skip
    def test01_shopping_cart(self):
        page = IdripMethod(self.idrip)
        page.email_login(email="louistest0625@gmail.com", password=711228)
        page.click_coffee_market()
        page.by_xpath_click("//android.view.View[@text='咖啡包']")
        page.by_xpath_click("//android.view.View[@text='G1極致 Top']")
        page.by_xpath_click("//android.view.View[@text='[陳志煌] 北歐烘焙風華配方 2013 北歐烘焙冠軍']")
        page.swipe_up(1000, 3)
        page.by_xpath_click("//android.view.View[@text='加入購物車']")
        time.sleep(2)
        for i in range(2):
            page.by_xpath_click("//android.view.View[@index='7']")
            time.sleep(1)
        page.by_xpath_click("//android.view.View[@text='確認']")
        time.sleep(0.5)
        toast = page.is_toast_exist("加入購物車完成")
        self.assertEqual(toast, True)

    def test02_market(self):
        page = IdripMethod(self.idrip)
        page.login("louistest0625@gmail.com", 711228)
        page.by_id_click("com.coffee.iDrip:id/linearLayout_shop")
        page.by_id_click("com.coffee.iDrip:id/textView_subtitle")
        page.by_id_click("com.coffee.iDrip:id/button")
        page.by_xpath_click("//android.widget.TextView[@text='香檳金']")
        page.by_id_click("com.coffee.iDrip:id/view_add")
        page.by_id_click("com.coffee.iDrip:id/button_ok")
        time.sleep(0.5)
        toast = page.is_toast_exist("購物車完成")
        self.assertEqual(toast, True)

    def test03_market(self):
        page = IdripMethod(self.idrip)
        page.login("louistest0625@gmail.com", 711228)
        page.by_xpath_click("//android.widget.TextView[@text='咖啡市集']")
        page.by_xpath_click("//android.widget.TextView[contains(@resource-id, 'packet') and @text='咖啡包']")
        page.swipe_up(500, 1)
        page.by_xpath_click("//android.widget.RelativeLayout[@index='2']")
        page.by_xpath_click("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                         "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                         ".FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android"
                                         ".widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget"
                                         ".RelativeLayout[2]/android.view.View[1]")
        page.by_id_click("com.coffee.iDrip:id/button_ok")
        toast = page.is_toast_exist("加入購物車完成")
        self.assertEqual(toast, True)


if __name__ == '__main__':
    unittest.main(verbosity=2)

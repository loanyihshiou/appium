# -*- coding: UTF-8 -*-
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'platformVersion': '6.0',
    # 'deviceName': '2bf04094591c7ece',
    'deviceName': 'Android emulator',
    'automationName': 'uiautomator2',
    'appPackage': 'com.android.calculator2',
    'appActivity': '.Calculator'}
web = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

web.find_element_by_id("com.android.calculator2:id/digit_6").click()
web.find_element_by_id("com.android.calculator2:id/op_add").click()
web.find_element_by_id("com.android.calculator2:id/digit_1").click()
web.find_element_by_id("com.android.calculator2:id/eq").click()
result = web.find_element_by_id("com.android.calculator2:id/formula").text

print(result)

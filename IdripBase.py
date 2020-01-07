from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class IdripMethod:

    def __init__(self, idrip):
        self.idrip = idrip

    def login(self, username, password):
        """Email登入"""
        self.idrip.find_element_by_id("com.coffee.iDrip:id/linearLayout_my").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/textView_name").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/textview_login").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/editText_email").send_keys(username)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/editText_pw").send_keys(password)
        self.idrip.find_element_by_id("com.coffee.iDrip:id/linearLayout_next").click()
        self.idrip.find_element_by_id("com.coffee.iDrip:id/textview_skip").click()

    def swipe_up(self, t, n):
        """向上滑動銀幕"""
        x = self.idrip.get_window_size()['width']
        y = self.idrip.get_window_size()['height']  # 取得螢幕長寬
        s = [x, y]
        sx1 = int(s[0] * 0.5)  # 起始x座標
        sy1 = int(s[1] * 0.75)  # 起始y座標
        sy2 = int(s[1] * 0.25)  # 終點y座標
        for i in range(n):
            time.sleep(1)
            self.idrip.swipe(sx1, sy1, sx1, sy2, t)  # t為滑動持續時間
            time.sleep(2)

    def swipe_down(self, t, n):  # t滑動時間 n滑動次數
        """向下滑動銀幕"""
        x = self.idrip.get_window_size()['width']
        y = self.idrip.get_window_size()['height']
        s = [x, y]
        sx1 = int(s[0] * 0.5)  # 起始x座標
        sy1 = int(s[1] * 0.25)  # 起始y座標
        sy2 = int(s[1] * 0.75)  # 終點y座標
        for i in range(n):
            time.sleep(1)
            self.idrip.swipe(sx1, sy1, sx1, sy2, t)  # t為滑動持續時間
            time.sleep(2)

    def is_toast_exist(self, text):
        """驗證toast文字"""
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)  # 抓取toast
            WebDriverWait(self.idrip, 10, 0.05).until(EC.presence_of_element_located(toast_loc))
            print(text)
            return True
        except:
            return False


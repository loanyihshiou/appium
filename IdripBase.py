from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class IdripMethod:

    def __init__(self, idrip):
        self.idrip = idrip

    def email_login(self, email, password):
        """Email登入"""
        self.idrip.find_element_by_xpath("//android.widget.ImageView[@text='我的']").click()
        self.idrip.find_element_by_xpath("//android.widget.ImageView[@text='我的訂單']").click()
        self.idrip.find_element_by_xpath("//android.view.View[@text='已有帳號登入']").click()
        self.idrip.find_element_by_xpath("//android.widget.EditText[@text='請輸入Email' and @index='2']").send_keys(email)
        self.idrip.find_element_by_xpath("//android.widget.EditText[@text='請輸入密碼' and @index='3']").send_keys(password)
        self.idrip.find_element_by_xpath("//android.view.View[@text='登入'and @index='4']").click()

    def click_coffee_market(self):
        self.idrip.find_element_by_xpath("//android.widget.ImageView[@text='咖啡市集']")

    def by_id_click(self, id_):
        """從ID找"""
        self.idrip.find_element_by_id(id_).click()

    def by_xpath_click(self, id_):
        """從XPATH找"""
        self.idrip.find_element_by_xpath(id_).click()

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

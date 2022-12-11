from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.base_page import BasePage


class IndexPage(BasePage):
    my_lemon_loc = (MobileBy.ID, 'com.lemon.lemonban:id/navigation_my')

    def click_my_lemon(self):
        """点击我的柠檬"""
        self.click_element(self.my_lemon_loc, '首页_我的柠檬')


class UserPage(BasePage):
    user_btn_loc = (By.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avatar_title')
    mobile_input_loc = (By.ID, 'com.lemon.lemonban:id/et_mobile')
    pwd_input_loc = (By.ID, 'com.lemon.lemonban:id/et_password')
    login_btn_loc = (By.ID, 'com.lemon.lemonban:id/btn_login')
    toast_loc = (By.XPATH, '//android.widget.Toast')

    def click_user_login(self):
        """点击头像登录"""
        self.click_element(self.user_btn_loc, '用户页面-点击头像登录')

    def login(self, user, pwd):
        """登录"""
        self.input_send_keys(self.mobile_input_loc, user, '用户页面-输入账号')
        self.input_send_keys(self.pwd_input_loc, pwd, '用户页面-输入密码')
        self.click_element(self.login_btn_loc, '用户页面-登录按钮')

    def is_login(self):
        try:
            text = self.get_element(self.user_btn_loc, '用户页面-用户头像信息')
        except:
            return False
        if text =='点击头像登录':
            return False
        else:
            return True

    def get_login_toast_info(self):
        """获取登录错误提示信息"""
        text = self.get_element_text(self.toast_loc, '用户登录页-toast弹窗提示')

        # text = WebDriverWait(self, 20, 0.5).until(EC.visibility_of_element_located(self.toast_loc))

        return text


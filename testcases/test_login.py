import time

import pytest
from appium.webdriver import Remote
from page.indexPage import IndexPage, UserPage
from datas.test_data import Login

@pytest.fixture()
def open_app():
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "11",
        "deviceName": "PCAM00",
        "appPackage": "com.lemon.lemonban",
        "appActivity": "com.lemon.lemonban.activity.MainActivity",

    }

    # 启动app
    driver = Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                    desired_capabilities=desired_cap)
    driver.implicitly_wait(15)
    yield driver


class TestLogin:
    @pytest.mark.parametrize('case', Login.success_test)
    def test_success_login(self, case, open_app):
        """测试成功登录"""
        driver = open_app
        # 点击我的柠檬
        IndexPage(driver).click_my_lemon()

        user_page = UserPage(driver)
        # 点击头像登录
        user_page.click_user_login()
        # 进行登录
        user_page.login(case['user'], case['pwd'])

        # 获取登录状态
        res = user_page.is_login()
        assert res == case['expected']

    @pytest.mark.parametrize('case', Login.fail_test)
    def test_success_pwd_is_none(self, case, open_app):
        """测试密码为空"""
        driver = open_app
        # 点击我的柠檬
        IndexPage(driver).click_my_lemon()

        user_page = UserPage(driver)
        # 点击头像登录
        user_page.click_user_login()
        # 进行登录
        user_page.login(case['user'], case['pwd'])

        # 获取页面上的错误提示信息
        res = user_page.get_login_toast_info()
        try:
            assert res == case['expected']
        except AssertionError as e:
            user_page.error_save_screenshot('{}断言失败'.format(case['title']))

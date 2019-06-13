# 登录测试用例
import unittest
from Business.Base_url import url
import ddt
from Common.tools.read_txt import read_txt
from HTMLReport import logger
from Page_Object.Common_Page.index_page import Index_Page
from Common.selenium_library import SeleniumBase
from Business.login_business import login


@ddt.ddt
class Test_login(unittest.TestCase):

    def setUp(self):
        self.driver = SeleniumBase().get_web_driver()

    def tearDown(self):

        SeleniumBase(self.driver).quit()

    @ddt.unpack
    @ddt.data(*read_txt('TestData/login_user_password.txt'))
    def test_login(self, username, password, assert_type):
        se = SeleniumBase(self.driver)
        se.get(url)
        login(self.driver, username, password)
        se.add_page_screen_shot()

        if assert_type == '1':
            logger().info("断言登陆成功")
            text = Index_Page(self.driver).login_success()

            self.assertIn("张维序", text, '登陆成功断言')

        elif assert_type == "2":
            text = self.driver.find_element_by_id("submit").text
            self.assertIn("立即登录", text, '登陆失败断言')

        elif assert_type == "3":
            text = self.driver.find_element_by_id("submit").text
            self.assertIn("立即登录", text, '登陆失败断言')

        elif assert_type == "4":
            text = self.driver.find_element_by_id("submit").text
            self.assertIn("立即登录", text, '登陆失败断言')

        else:
            logger().info(f"未知断言类型{assert_type}")
            self.assertTrue(False, "未知断言类型")

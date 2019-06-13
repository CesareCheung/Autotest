import time
import unittest
import ddt
from Business.Base_url import url
from Common.tools.read_txt import read_txt
from Business.login_business import login
from Common.selenium_library import SeleniumBase
from Page_Object.Business_Page.business_page import BusinessPage
from Page_Object.Business_Page.Lines_Page.lines_type_page import Lines_Type
from Page_Object.Common_Page.index_page import Index_Page
from Page_Object.Business_Page.Lines_Page.journey_page import Journey_Page
from Business.sync_user_data import acquire_user, release_user


@ddt.ddt
class Test_Business(unittest.TestCase):
    '''业务-线路产品管理测试类'''

    def setUp(self):
        self.k, self.user = acquire_user("TestData/user.txt")
        self.driver = SeleniumBase().get_web_driver()

    def tearDown(self):
        release_user(self.k)
        SeleniumBase(self.driver).quit()

    @ddt.unpack
    @ddt.data(*read_txt('TestData/lines_type.txt'))
    def test_add_line_type(self, name, ename, tag_name):
        '''添加线路类别'''
        try:
            username, password = self.user
            se = SeleniumBase(self.driver)
            se.get(url)
            login(self.driver, username, password)
            index = Index_Page(self.driver)
            index.click_business()
            Business = BusinessPage(self.driver)
            Business.click_lines()
            line_type = Lines_Type(self.driver)
            line_type.click_line_type()
            self.driver.switch_to.frame(0)
            self.driver.switch_to.frame(0)
            line_type.click_add_lines()
            se.add_page_screen_shot()
            line_type.add_lines_type_msg(name, ename, tag_name)
            se.add_page_screen_shot()
        except Exception:
            raise ("添加线路类别异常")


    @ddt.unpack
    @ddt.data(*read_txt('TestData/add_trip.txt'))
    def test_add_trip(self, trip, dinner, hotel, traffic, travel):
        '''添加线路行程'''
        try:
            username, password = self.user
            se = SeleniumBase(self.driver)
            se.get(url)
            login(self.driver, username, password)
            index = Index_Page(self.driver)
            index.click_business()
            Business = BusinessPage(self.driver)
            Business.click_lines()
            Journey = Journey_Page(self.driver)
            Journey.click_journey()
            se.add_page_screen_shot()
            self.driver.switch_to.frame(0)
            self.driver.switch_to.frame(0)
            Journey.add_journey(trip, dinner, hotel, traffic, travel)
            se.add_page_screen_shot()
        except Exception:
            raise ('添加线路行程异常')

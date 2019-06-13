import unittest
import ddt
from Business.Base_url import url
from Business.login_business import login
from Business.sync_user_data import acquire_user, release_user
from Common.selenium_library import SeleniumBase
from Common.tools.read_txt import read_txt
from Page_Object.Business_Page.business_page import BusinessPage
from Page_Object.Common_Page.index_page import Index_Page
from Page_Object.Business_Page.Ticket_mana_Page.flight_mana_page import Flight_Mana_Page

# 通过ddt模块调取TestData数据
@ddt.ddt
class Test_Itinerary_Test(unittest.TestCase):
    '''添加机票行程'''

    def setUp(self):
        self.k, self.user = acquire_user('TestData/user.txt')
        self.driver = SeleniumBase().get_web_driver()

    def tearDown(self):
        release_user(self.k)
        self.driver.quit()

    @ddt.unpack
    @ddt.data(*read_txt('TestData/itinerary.txt'))
    def test_add_itinerary(self, itinerary_name, routes, itinerary_day, remark1):
        try:
            username, password = self.user
            se = SeleniumBase(self.driver)
            se.get(url)
            login(self.driver, username, password)
            index = Index_Page(self.driver)
            index.click_business()
            Business = BusinessPage(self.driver)
            Business.click_air_ticket()

            Flight = Flight_Mana_Page(self.driver)
            Flight.air_mana()
            self.driver.switch_to.frame(0)
            self.driver.switch_to.frame(0)
            Flight.click_itinerary()
            Flight.add_itnerary(itinerary_name, routes, itinerary_day, remark1)
        except Exception:
            raise ("测试出现异常")

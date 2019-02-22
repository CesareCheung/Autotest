from selenium.webdriver.common.by import By
from Page_Object.Common_Page.index_page import Index_Page
from Common.selenium_library import SeleniumBase



class Flight_Mana_Page(SeleniumBase):
    loc_air_mana=(By.LINK_TEXT,'机票行程管理')
    loc_itinerary=(By.ID,'btn_add-btnInnerEl')
    loc_itinerary_name=(By.ID,'title-inputEl')
    loc_routes=(By.ID,'route-inputEl')
    loc_routes_days=(By.ID,'days-inputEl')
    loc_remark=(By.ID,'theDesc-inputEl')
    loc_save_itinerary=(By.ID,'button-1013-btnInnerEl')

    def air_mana(self):
        self.logger.info("点击机票行程管理")
        self.click_element(self.loc_air_mana)


    def click_itinerary(self):
        self.logger.info('添加行程')
        self.click_element(self.loc_itinerary)

    def add_itnerary(self,itinerary_name,routes,itinerary_day,remark1):
        self.logger.info('添加行程数据并保存')
        self.send_keys(self.loc_itinerary_name,itinerary_name)
        self.send_keys(self.loc_routes,routes)
        self.send_keys(self.loc_routes_days,itinerary_day)
        self.send_keys(self.loc_remark,remark1)
        self.click_element(self.loc_save_itinerary)


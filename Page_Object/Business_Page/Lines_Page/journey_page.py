from selenium.webdriver.common.by import By
from Common.selenium_library import SeleniumBase

class Journey_Page(SeleniumBase):
    """添加行程模板页面"""
    loc_journey=(By.LINK_TEXT,'行程模板')
    loc_add_trip=(By.ID,'trip_item_day_btn_add-btnInnerEl')
    loc_trip=(By.ID,'trip_item_day_outline-inputEl')
    loc_dinner=(By.ID,'trip_item_day_dining-inputEl')
    loc_hotel=(By.ID,'trip_item_day_hotel-inputEl')
    loc_traffic=(By.ID,'trip_item_day_traffic-inputEl')
    loc_travel=(By.ID,'trip_item_day_dimension-inputEl')
    loc_save_trip=(By.ID,'button-1010-btnEl')


    def click_journey(self):
        self.logger.info('点击行程管理')
        self.click_element(self.loc_journey)


    def add_journey(self,trip,dinner,hotel,traffic,travel):
        self.logger.info('点击添加行程按钮')
        self.click_element(self.loc_add_trip)
        self.logger.info(f"行程概要：{trip},用餐:{dinner},住宿:{hotel},交通:{traffic},行程内容:{travel}")
        self.send_keys(self.loc_trip,trip)
        self.send_keys(self.loc_dinner,dinner)
        self.send_keys(self.loc_hotel,hotel)
        self.send_keys(self.loc_traffic,traffic)
        self.send_keys(self.loc_travel,travel)
        self.logger.info("点击保存按钮")
        self.click_element(self.loc_save_trip)

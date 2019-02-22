from Common.selenium_library import SeleniumBase
from selenium.webdriver.common.by import By

class Line_Manage_Page(SeleniumBase):
    """线路管理页面"""
    loc_click_add_line = (By.ID, "btn_new-btnInnerEl")
    loc_line_type_click=(By.ID,'ext-gen1645')
    loc_line_options=(By.CLASS_NAME,'x-boundlist-list-ct')
    loc_line_name=(By.ID,'title')

    def add_line_manage(self):
        self.logger.info('添加线路管理')
        self.click_element(self.loc_click_add_line)

    def add_lines_manage_msg(self,linename):
        """"""
        self.logger.info('添加线路信息')
        self.click_element(self.loc_line_type_click)
        self.select_from_list_by_index(self.loc_line_options,2)
        self.send_keys(self.loc_line_name,linename)







import time

from Common.selenium_library import SeleniumBase
from selenium.webdriver.common.by import By


class Lines_Type(SeleniumBase):
    """线路类别页面"""
    loc_lines_type = (By.LINK_TEXT, '线路类别')
    loc_add_line = (By.ID, 'btn_grid_list_new-btnInnerEl')
    loc_lines_name = (By.ID, 'win_item_web_cnName-inputEl')
    loc_lines_ename = (By.ID, 'win_item_web_code-inputEl')
    loc_lines_tag_name = (By.ID, 'win_item_web_tags-inputEl')
    loc_save_add_lines = (By.ID, 'button-1052-btnInnerEl')

    def click_line_type(self):
        self.logger.info("点击线路类别")
        self.click_element(self.loc_lines_type)

    def click_add_lines(self):
        self.logger.info("点击添加线路类别按钮")
        self.click_element(self.loc_add_line)

    def add_lines_type_msg(self, name, ename, tag_name):
        self.send_keys(self.loc_lines_name, name)
        self.send_keys(self.loc_lines_ename, ename)
        self.send_keys(self.loc_lines_tag_name, tag_name)
        self.logger.info(f"添加线路类别名称{name},英文名称{ename},标签名称{tag_name}")
        self.logger.info('点击保存按钮')
        self.click_element(self.loc_save_add_lines)

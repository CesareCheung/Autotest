from Common.selenium_library import SeleniumBase
from selenium.webdriver.common.by import By


class Index_Page(SeleniumBase):
    """首页页面对象"""
    login_loc = (By.ID, "index_my_username")
    business_loc = (By.LINK_TEXT, "业务")
    customer_loc = (By.LINK_TEXT, "客户")
    resource_loc = (By.LINK_TEXT, "资源")
    finance_loc = (By.LINK_TEXT, "财务")
    stat_loc = (By.LINK_TEXT, "统计")
    abutment_loc = (By.LINK_TEXT, "对接")
    sys_loc = (By.LINK_TEXT, "系统")
    website_loc = (By.LINK_TEXT, "网站")
    operate_loc = (By.LINK_TEXT, "运营")
    supplier_loc = (By.LINK_TEXT, "供应商")
    distri_loc = (By.LINK_TEXT, "门店")

    def login_success(self):
        self.logger.info('返回登录成功校验文本值')
        return self.get_element_text(self.login_loc)

    def click_business(self):
        self.logger.info("点击业务模块")
        self.click_element(self.business_loc)

    def click_customer(self):
        self.logger.info("点击客户模块")
        self.click_element(self.customer_loc)

    def click_resource(self):
        self.logger.info("点击资源模块")
        self.click_element(self.resource_loc)

    def click_finance(self):
        self.logger.info("点击财务模块")
        self.click_element(self.finance_loc)

    def click_stat(self):
        self.logger.info("点击统计模块")
        self.click_element(self.stat_loc)

    def click_abutment(self):
        self.logger.info("点击对接模块")
        self.click_element(self.abutment_loc)

    def click_sys(self):
        self.logger.info("点击系统模块")
        self.click_element(self.sys_loc)

    def click_website(self):
        self.logger.info("点击网站模块")
        self.click_element(self.website_loc)

    def click_operate(self):
        self.logger.info("点击运营模块")
        self.click_element(self.operate_loc)

    def click_supplier(self):
        self.logger.info("点击供应商模块")
        self.click_element(self.supplier_loc)

    def click_distri(self):
        self.logger.info("点击门店模块")
        self.click_element(self.distri_loc)

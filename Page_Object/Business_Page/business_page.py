from Common.selenium_library import SeleniumBase
from selenium.webdriver.common.by import By
from Page_Object.Common_Page.index_page import Index_Page


class BusinessPage(SeleniumBase):
    """业务页面对象"""
    loc_lines=(By.LINK_TEXT,'线路产品管理')
    loc_air=(By.LINK_TEXT,'机票管理')
    loc_plan=(By.LINK_TEXT,'团期计划')
    loc_order=(By.LINK_TEXT,'订单管理')
    loc_single=(By.LINK_TEXT,'单项业务')
    loc_team_offer=(By.LINK_TEXT,'团队报价')
    loc_bill_review=(By.LINK_TEXT,'账单审核')
    loc_cost_audit=(By.LINK_TEXT,'成本审核')
    loc_guide_submit=(By.LINK_TEXT,'导游报账')
    loc_audit_invoice=(By.LINK_TEXT,'发票申请')
    loc_pending_matters=(By.LINK_TEXT,'待处理事项')
    loc_team_sum=(By.LINK_TEXT,"团队汇总")

    def click_lines(self):
        self.logger.info('点击线路产品管理')
        self.click_element(self.loc_lines)

    def click_air_ticket(self):
        self.logger.info("点击机票管理")
        self.click_element(self.loc_air)

    def click_group_plan(self):
        self.logger.info("点击团期计划")
        self.click_element(self.loc_plan)

    def click_order(self):
        self.logger.info('点击订单管理')
        self.click_element(self.loc_order)

    def click_single(self):
        self.logger.info('点击单项业务')
        self.click_element(self.loc_single)

    def click_team_offer(self):
        self.logger.info("点击团队报价")
        self.click_element(self.loc_team_offer)

    def click_bill_review(self):
        self.logger.info("点击账单审核")
        self.click_element(self.loc_bill_review)

    def click_cost_audit(self):
        self.logger.info("点击成本审核")
        self.click_element(self.loc_cost_audit)

    def click_guide_submit(self):
        self.logger.info("点击导游报账")
        self.click_element(self.loc_guide_submit)

    def click_audit_invoice(self):
        self.logger.info("点击发票申请")
        self.click_element(self.loc_audit_invoice)

    def click_pending_matters(self):
        self.logger.info("点击待处理事项")
        self.click_element(self.loc_pending_matters)

    def click_team_sum(self):
        self.logger.info("点击团队汇总")
        self.click_element(self.loc_team_sum)

"""Selenium 封装基类

封装查找元素以及集成日志输出"""
from HTMLReport import logger
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class Base(object):
    def __init__(self, driver: webdriver.Remote = None):
        self.driver = driver
        self.logger = logger()

    def find_element(self, locator: tuple) -> WebElement:
        """查找单个元素

        :param locator: 定位器（by=By.ID, value=None）
        :return: WebElement
        """
        self.logger.info(f"查找元素：{locator}")
        try:
            element = self.driver.find_element(*locator)
        except Exception:
            self.logger.info("查找元素失败")
            raise
        else:
            self.logger.info("查找元素成功")
        return element

    def find_elements(self, locator: tuple):
        """查找元素集合

        :param locator: 定位器（by=By.ID, value=None）
        :return: 元素对象集合
        :rtype: list of WebElement
        """
        self.logger.info(f"查找元素集合：{locator}")
        elements = self.driver.find_elements(*locator)
        self.logger.info(f"查找到{len(elements)}个元素")
        return elements

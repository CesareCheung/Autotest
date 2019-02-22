from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base import Base


class Element(Base):
    """
    元素类
    """

    def is_element(self, locator, time_out=0) -> bool:
        """判断页面是否存在该元素

        元素存在返回True，否则返回False

        :param locator: 定位器 (by=By.ID, value=None)
        :param time_out: 超时，默认 0
        :return:
        """
        self.logger.info(f"判断页面是否存在元素：{locator}")
        try:
            WebDriverWait(self.driver, time_out).until(
                EC.presence_of_element_located(locator)
            )
        except NoSuchElementException:
            self.logger.info("元素不存在")
            return False
        else:
            self.logger.info("元素存在")
        return True

    def get_element_attribute(self, locator, attribute):
        """返回元素的属性值

        :param locator: 定位器 (by=By.ID, value=None)
        :param attribute: 属性名
        :return:
        """
        if not attribute:
            raise ValueError("attribute 值不能为空")
        attribute_text = self.find_element(locator).get_attribute(attribute)
        self.logger.info(f"返回元素 {attribute} 属性值：{attribute_text}")
        return attribute_text

    def get_element_rect(self, locator):
        """获取元素大小以及位置

        :param locator: 定位器 (by=By.ID, value=None)
        :return: 一个具有元素大小和位置的字典。
        """
        rect = self.find_element(locator).rect
        self.logger.info(f"获取元素大小以及位置 {rect}")
        return rect

    def get_element_text(self, locator):
        """获取元素的文本值

        :param locator: 定位器 (by=By.ID, value=None)
        :return:
        """
        text = self.find_element(locator).text
        self.logger.info(f"获取元素的文本值：{text}")
        return text

    def get_element_value(self, locator):
        """获取元素的 value 值

        :param locator: 定位器 (by=By.ID, value=None)
        :return:
        """
        value = self.get_element_attribute(locator, "value")
        self.logger.info(f"获取元素的 value 值：{value}")
        return value

    def clear_element_text(self, locator):
        """清空元素的文本值"""
        self.logger.info(f"清空元素：{locator}的文本值")
        self.find_element(locator).clear()

    def click_element(self, locator):
        """点击元素"""
        self.logger.info(f"点击元素：{locator}")
        self.find_element(locator).click()

    def double_click_element(self, locator):
        """双击元素"""
        self.logger.info(f"双击元素：{locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def scroll_element_into_view(self, locator):
        """滚动到元素"""
        self.logger.info(f"滚动到元素：{locator}")
        element = self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def drag_and_drop(self, locator, target):
        """拖拽元素

        :param locator: 被拖拽元素定位器
        :param target: 目标元素定位器
        :return:
        """
        self.logger.info(f"拖拽元素：{locator} --> {target}")
        element = self.find_element(locator)
        target = self.find_element(target)
        action = ActionChains(self.driver)
        action.drag_and_drop(element, target).perform()

    def drag_and_drop_by_offset(self, locator, xoffset: int, yoffset: int):
        """拖拽一个元素到一个偏移量

        :param locator: 元素定位器
        :param xoffset: x轴偏移量
        :param yoffset: y轴偏移量
        :return:
        """
        self.logger.info(f"拖拽元素：{locator} 到偏移量：{(xoffset, yoffset)}")
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, xoffset, yoffset)
        action.perform()

    def mouse_down(self, locator):
        """在元素上按下鼠标左键，并保持"""
        self.logger.info(f"在元素上按下鼠标左键：{locator}")
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.click_and_hold(element).perform()

    def mouse_out(self, locator):
        """移动鼠标离开元素"""
        self.logger.info(f"移动鼠标离开元素：{locator}")
        element = self.find_element(locator)
        size = element.size
        offsetx = (size['width'] / 2) + 1
        offsety = (size['height'] / 2) + 1
        action = ActionChains(self.driver)
        action.move_to_element(element).move_by_offset(offsetx, offsety)
        action.perform()

    def mouse_over(self, locator):
        """鼠标悬浮在元素上"""
        self.logger.info(f"鼠标悬浮在元素上：{locator}")
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def mouse_up(self, locator=None):
        """释放鼠标左键"""
        if not locator:
            self.logger.info(f"释放鼠标左键：{locator}")
            element = self.find_element(locator)
            ActionChains(self.driver).release(element).perform()
        else:
            ActionChains(self.driver).release().perform()

    def send_keys(self, locator, *value):
        """清空原有内容，发送文本或按键到元素上"""
        self.logger.info(f"发送文本或按键：{value} 到元素上：{locator}")
        element = self.find_element(locator)
        element.clear()
        element.send_keys(*value)

    def select_box(self, locator):
        """选择“定位器”标识的选择框。

        如果选择框已经被选中，则什么都不做。
        """
        self.logger.info(f"选择 选择框：{locator}")
        element = self.find_element(locator)
        if not element.is_selected():
            element.click()

    def un_select_box(self, locator):
        """移除“定位器”标识的选择的选择。

        如果选择框没有被选中，则什么都不做。
        """
        self.logger.info(f"取消选择 选择框：{locator}")
        element = self.find_element(locator)
        if element.is_selected():
            element.click()

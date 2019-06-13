# 下拉列表选择封装
from selenium.webdriver.support.select import Select

from .base import Base


class SelectElement(Base):

    def get_list_items(self, locator, values: bool = False):
        """返回下拉列表的可见文本或value属性值，默认返回 value值

        :param locator: 定位方式元组
        :param values: 为 True 返回 可见文本
        :rtype: list of str
        """
        options = self._get_options(locator)
        if values:
            return self._get_texts(options)
        else:
            return self._get_values(options)

    def get_selected_list_text(self, locator):
        """返回下拉列表的已选择选项的文本值

        如果选择了多个选项，返回第一个选项的文本值
        """
        select = self._get_select_list(locator)
        return select.first_selected_option.text

    def get_selected_list_texts(self, locator):
        """返回下拉列表的已选择项的所有文本值

        返回值为列表

        :param locator:
        :return:
        """
        options = self._get_selected_options(locator)
        return self._get_texts(options)

    def get_selected_list_value(self, locator):
        """返回下拉列表的已选择选项的value属性值

        如果选择了多个选项，返回第一个选项的value属性值"""
        select = self._get_select_list(locator)
        return select.first_selected_option.get_attribute('value')

    def get_selected_list_values(self, locator):
        """返回下拉列表的已选择项的所有value属性值

        返回值为列表"""
        options = self._get_selected_options(locator)
        return self._get_values(options)

    def select_all_from_list(self, locator):
        """选择多选下拉列表所有选项"""
        self.logger.info(f"选择下拉列表:{locator} 所有选项")
        select = self._get_select_list(locator)
        if not select.is_multiple:
            raise RuntimeError("select_all_from_list 只能在多选下拉列表中使用")
        for i in range(len(select.options)):
            select.select_by_index(i)

    def select_from_list_by_index(self, locator, *indexes):
        """通过 index 选择下拉列表选项

        列表选项的索引从0开始。

        如果一个单选择列表需要选择多个选项，最后一个值将被选中。

        多选列表将选择所有 indexes 参数的选项，但是旧选择可能不清除。

        :param locator: 定位
        :param indexes: 需要选中的列表项的索引
        :return:
        """
        if not indexes:
            raise ValueError("indexes 参数不能为空")
        self.logger.info(f"对下拉列表：{locator}，通过 index 选择：{indexes}")
        select = self._get_select_list(locator)
        for index in indexes:
            select.select_by_index(int(index))

    def select_from_list_by_value(self, locator, *values):
        """通过 value属性值 选择下拉列表选项

        如果一个单选择列表需要选择多个选项，最后一个值将被选中。

        多选列表将选择所有 values 参数的选项，但是旧选择可能不清除。
        
        :param locator: 定位
        :param values: 需要选中的列表项的value属性值
        :return: 
        """
        if not values:
            raise ValueError("values 参数不能为空")
        self.logger.info(f"对下拉列表：{locator}，通过 value属性值选择：{values}")
        select = self._get_select_list(locator)
        for value in values:
            select.select_by_value(value)

    def select_from_list_by_text(self, locator, *text):
        """通过 文本内容 选择下拉列表选项

        如果一个单选择列表需要选择多个选项，最后一个值将被选中。

        多选列表将选择所有 text 参数的选项，但是旧选择可能不清除。
        
        :param locator: 定位
        :param text: 文本内容
        :return: 
        """
        if not text:
            raise ValueError("text 参数不能为空")
        self.logger.info(f"对下拉列表：{locator}，通过 文本内容选择：{text}")
        select = self._get_select_list(locator)
        for label in text:
            select.select_by_visible_text(label)

    def unselect_all_from_list(self, locator):
        """取消下拉列表所有选项，本方法只对多选下拉列表生效
        
        :param locator: 定位
        :return: 
        """
        self.logger.info(f"取消下拉列表所有选择项：{locator}")
        select = self._get_select_list(locator)
        if not select.is_multiple:
            raise RuntimeError("unselect_all_from_list 只能在多选下拉列表中使用")
        select.deselect_all()

    def unselect_from_list_by_index(self, locator, *indexes):
        """通过 index 取消多选下拉列表的选择项

        列表选项的索引从0开始。

        本方法只适用于多选下拉列表。

        :param locator: 定位
        :param indexes: 索引
        :return:
        """
        if not indexes:
            raise ValueError("indexes 参数不能为空")
        self.logger.info(f"对下拉列表：{locator}，通过 index 取消已选项：{indexes}")
        select = self._get_select_list(locator)
        if not select.is_multiple:
            raise RuntimeError("unselect_from_list_by_index 只能在多选下拉列表中使用")

        for index in indexes:
            select.deselect_by_index(int(index))

    def unselect_from_list_by_value(self, locator, *values):
        """通过 value属性值 取消多选下拉列表的选择项

        本方法只适用于多选下拉列表。

        :param locator: 定位
        :param values: value属性值
        :return:
        """
        if not values:
            raise ValueError("values 参数不能为空")
        self.logger.info(f"对于下拉列表：{locator}，通过 value属性值取消选择项：{values}")
        select = self._get_select_list(locator)
        if not select.is_multiple:
            raise RuntimeError("unselect_from_list_by_value 只能在多选下拉列表中使用")

        for value in values:
            select.deselect_by_value(value)

    def unselect_from_list_by_text(self, locator, *texts):
        """通过 文本内容 取消多选下拉列表的选择项

        本方法只适用于多选下拉列表。

        :param locator: 定位
        :param texts: 文本内容
        :return:
        """

        if not texts:
            raise ValueError("texts 参数不能为空")
        self.logger.info(f"对于下拉列表：{locator}，通过文本内容取消选择项：{texts}")
        select = self._get_select_list(locator)
        if not select.is_multiple:
            raise RuntimeError("unselect_from_list_by_text 只能在多选下拉列表中使用")

        for text in texts:
            select.deselect_by_visible_text(text)

    def _get_select_list(self, locator):
        el = self.find_element(locator)
        return Select(el)

    def _get_options(self, locator):
        return self._get_select_list(locator).options

    def _get_selected_options(self, locator):
        return self._get_select_list(locator).all_selected_options

    def _get_texts(self, options):
        return [opt.text for opt in options]

    def _get_values(self, options):
        return [opt.get_attribute('value') for opt in options]

# 截图方法封装
from HTMLReport import AddImage

from .base import Base


class Screenshot(Base):
    def add_page_screen_shot(self, title="", describe=""):
        """添加页面截图到报告中

        注意，如果存在警告信息，将截屏失败，导致测试终止

        :param title: 图片标题
        :param describe: 图片提示
        """
        self.logger.info(f"添加截图到报告中 {title}")
        AddImage(self.driver.get_screenshot_as_base64(), title, describe)

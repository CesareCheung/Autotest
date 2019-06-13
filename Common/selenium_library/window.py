# 浏览器窗口操作封装
from .base import Base


class Window(Base):
    def close_window(self):
        """关闭当前窗口"""
        self.logger.info(f"关闭窗口：{self.driver.title}")
        self.driver.close()

    def switch_to_window_url(self, url):
        """通过 URL 包含关系跳转到新标签页

        :param url: 网址的一部分即可
        :return:
        """
        self.logger.info(f"根据URL跳转标签页：{url}")
        if url in self.driver.current_url:
            return
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if url in self.driver.current_url:
                return
        raise RuntimeError(f"找不到 url 包含：{url} 的标签页")

    def switch_to_window_title(self, title):
        """通过 title 包含关系跳转到新标签页

        :param title: 网址的一部分即可
        :return:
        """
        self.logger.info(f"根据 title 跳转标签页：{title}")
        if title in self.driver.current_url:
            return
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title in self.driver.title:
                return
        raise RuntimeError(f"找不到 title 包含：{title} 的标签页")

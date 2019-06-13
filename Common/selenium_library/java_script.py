# 执行JS操作封装
from .base import Base


class JavaScript(Base):
    def execute_javascript(self, js):
        """执行 JavaScript"""
        self.logger.info(f"执行 JavaScript:\n{js}")
        return self.driver.execute_script(js)

    def execute_async_javascript(self, js):
        """执行异步 JavaScript"""
        self.logger.info(f"执行异步 JavaScript:\n{js}")
        return self.driver.execute_async_script(js)

# 对cookie操作封装
from .base import Base


class Cookie(Base):
    def add_cookie(self, name: str, value: str, path: str = None, domain: str = None, secure: bool = None,
                   expiry=None):
        """在当前的会话中添加一个cookie。"""
        new_cookie = {'name': name, 'value': value}
        if not path:
            new_cookie['path'] = path
        if not domain:
            new_cookie['domain'] = domain
        # Secure must be True or False
        if not secure:
            new_cookie['secure'] = secure
        if not expiry:
            new_cookie['expiry'] = expiry
        self.logger.info(f"添加 cookie：\n{new_cookie}")
        self.driver.add_cookie(new_cookie)

    def delete_cookie(self, name):
        """删除cookie匹配的“name”。

        如果没有找到cookie，什么也不会发生。
        """
        self.logger.info(f"删除cookie：{name}")
        self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        """删除所有cookie。"""
        self.logger.info("删除所有cookie")
        self.driver.delete_all_cookies()

    def get_cookie(self, name):
        """返回“name”匹配的cookie
        """
        cookie = self.driver.get_cookie(name)
        self.logger.info(f'获取 name = {name} 的cookie：\n{cookie}')
        return cookie

    def get_cookies(self):
        """返回当前页面的所有cookie。"""
        cookies = self.driver.get_cookies()
        self.logger.info(f"获取所有cookies：\n{cookies}")
        return cookies

from selenium.webdriver.common.by import By

from Common.selenium_library import SeleniumBase


class Login_Page(SeleniumBase):
    """登录页面对象"""
    loc_user = (By.ID, "username")
    loc_psw = (By.ID, "password")
    loc_sub = (By.ID, "submit")

    def send_username(self, username):
        self.logger.info(f"输入用户名{username}")
        self.send_keys(self.loc_user, username)

    def send_password(self, password):
        self.logger.info(f"输入密码{password}")
        self.send_keys(self.loc_psw, password)

    def submit(self):
        self.logger.info("点击登录按钮")
        self.click_element(self.loc_sub)

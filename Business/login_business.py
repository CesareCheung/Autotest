# 登录公共模块业务流，用于执行测试用例前调用进行账户的登录

from Page_Object.Common_Page.login_page import Login_Page
from HTMLReport import logger
import time


def login(driver, username, password):
    """
    登录业务
    :param driver:浏览器驱动
    :param username:用户名
    :param password:密码
    :return:None
    """
    logger().info(f"使用用户名:{username},密码:{password}进行登陆")
    login_page = Login_Page(driver)
    login_page.send_username(username)
    login_page.send_password(password)
    login_page.submit()
    time.sleep(2)

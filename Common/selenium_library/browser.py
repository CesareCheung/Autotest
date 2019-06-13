"""
获取浏览器
    打开本地浏览器
    打开远程浏览器
关闭浏览器
打开网址
最大化
最小化
标题
url
刷新

"""
from selenium import webdriver

from Common.tools.rw_ini import read_config
from .base import Base


class Browser(Base):
    def get_web_driver(self) -> webdriver.Remote:
        """获取浏览器实例

        :return: 浏览器实例
        """
        rc = read_config("browser.ini")
        local_browser = rc.getboolean("local", "local_browser", fallback=True)
        wait_time = rc.getint("local", "wait_time", fallback=10)

        browser_name = rc.get("browser", "name", fallback="chrome")
        window_width = rc.get("browser", "window_width", fallback=None)
        window_height = rc.get("browser", "window_height", fallback=None)

        command_executor = rc.get("grid", "command_executor", fallback="http://127.0.0.1:4444/wd/hub")
        headless = rc.getboolean("grid", "headless", fallback=False)
        proxy = rc.get("grid", "proxy", fallback=None)

        if local_browser:
            # 打开本地浏览器
            driver = self._get_local_web_driver(browser_name)
        else:
            # 打开远程浏览器
            driver = self._get_remote_web_driver(browser_name, command_executor, headless, proxy)
        self.logger.info(f"打开浏览器：{driver.name}")

        self.logger.info(f"设置隐式等待：{wait_time}s")
        driver.implicitly_wait(wait_time)

        if window_width is None or window_width == "" or window_height is None or window_height == "":
            self.logger.info("最大化浏览器")
            driver.maximize_window()
        else:
            driver.set_window_size(window_width, window_height)
        return driver

    def _get_local_web_driver(self, browser_name: str) -> webdriver.Remote:
        """获取本地浏览器实例

        :param browser_name: 浏览器类型
        :return: 浏览器实例
        """
        if browser_name.upper() == "CHROME":
            driver = webdriver.Chrome()
        elif browser_name.upper() == "FIREFOX":
            driver = webdriver.Firefox()
        elif browser_name.upper() == "IE":
            driver = webdriver.Ie()
        else:
            self.logger.error(f"浏览器类型错误：{browser_name}")
            raise ValueError(f"浏览器类型错误：{browser_name}")
        return driver

    def _get_remote_web_driver(self, browser_name, command_executor, headless, proxy) -> webdriver.Remote:
        """获取远程浏览器实例

        :param browser_name: 浏览器类型
        :param command_executor: HUB 地址
        :param headless: 使用无头浏览器
        :param proxy: 代理
        :return: 浏览器实例
        """
        if browser_name.upper() == "CHROME":
            options = webdriver.ChromeOptions()
        elif browser_name.upper() == "FIREFOX":
            options = webdriver.FirefoxOptions()
        elif browser_name.upper() == "IE":
            options = webdriver.IeOptions()
        else:
            self.logger.error(f"浏览器类型错误：{browser_name}")
            raise ValueError(f"浏览器类型错误：{browser_name}")

        if proxy is not None:
            options.add_argument(f"--proxy-server={proxy}")
        # 无头浏览器
        options.headless = headless

        driver = webdriver.Remote(
            command_executor=command_executor,
            options=options
        )
        return driver

    def quit(self):
        """退出浏览器"""
        self.logger.info(f"关闭浏览器：{self.driver.name}")
        self.driver.quit()

    def get(self, url: str, new: bool = False):
        """打开 url

        :param url: 网址
        :param new: 是否新窗口打开
        :return: None
        """
        if new:
            self.logger.info(f"新窗口打开 url：{url}")
            self.driver.execute_script(f"window.open('{url}')")
        else:
            self.logger.info(f"当前窗口打开 url：{url}")
            self.driver.get(url)

    def get_session_id(self):
        """返回当前浏览器 session id"""
        session_id = self.driver.session_id
        self.logger.info(f"当前浏览器 session_id：{session_id}")
        return session_id

    def get_source(self) -> str:
        """获取当前页面HTML源代码"""
        page_source = self.driver.page_source
        self.logger.info(f"当前页面源代码：\n{page_source}")
        return page_source

    def get_title(self):
        """返回当前页面的标题"""
        title = self.driver.title
        self.logger.info(f"当前页面的标题：{title}")
        return title

    def get_current_url(self):
        """返回当前页面的URL"""
        current_url = self.driver.current_url
        self.logger.info(f"当前页面URL：{current_url}")
        return current_url

    def reload_page(self):
        """模拟用户重新加载页面"""
        self.logger.info("刷新页面")
        self.driver.refresh()

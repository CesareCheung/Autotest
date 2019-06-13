#  警告弹框处理封装
from selenium.common.exceptions import TimeoutException
from .base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert as Alert_


class Alert(Base):
    """警告框"""
    ACCEPT = 'ACCEPT'
    DISMISS = 'DISMISS'
    LEAVE = 'LEAVE'

    def input_text_into_alert(self, text: str, action=ACCEPT, timeout=10):
        """将给定的文本输入到警告框中

        :param text: 文本内容
        :param action: 可选值：ACCEPT（接收）、DISMISS（取消）、LEAVE（保持不处理）
        :param timeout: 等待警告框出现的延迟
        :return: None
        """
        self.logger.info(f"发送内容到警告框：{text}")
        alert = self._wait_alert(timeout)
        alert.send_keys(text)
        self._handle_alert(alert, action)

    def is_alert(self, timeout=0) -> bool:
        """判断警告框是否存在

        :param timeout: 延迟
        :return: bool
        """
        try:
            self._wait_alert(timeout)
        except TimeoutException:
            return False
        else:
            return True

    def handle_alert(self, action=ACCEPT, timeout=10) -> str:
        """处理当前警告框并返回它的消息

        :param action: 可选值：ACCEPT（接收）、DISMISS（取消）、LEAVE（保持不处理）
        :param timeout: 等待警告框出现的延迟
        :return: 文本
        """
        alert = self._wait_alert(timeout)
        return self._handle_alert(alert, action)

    def _wait_alert(self, timeout) -> Alert_:
        """等待警告框出现

        :param timeout: 超时时间
        :return: 警告框对象
        """
        wait = WebDriverWait(self.driver, timeout)
        try:
            alert = wait.until(ec.alert_is_present())
        except TimeoutException:
            self.logger.error(f"{timeout}s 内警告框没有出现")
            raise
        else:
            self.logger.info("发现警告框")
        return alert

    def _handle_alert(self, alert: Alert_, action: str) -> str:
        """处理警告框并返回警告框文本内容"""
        action = action.upper()
        text = alert.text
        if action == self.ACCEPT:
            self.logger.info("接受警告框")
            alert.accept()
        elif action == self.DISMISS:
            self.logger.info("取消警告框")
            alert.dismiss()
        elif action != self.LEAVE:
            raise ValueError(f"无效的警告框处理行为：{action}")
        return text

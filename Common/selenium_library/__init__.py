from .alert import Alert
from .browser import Browser
from .cookie import Cookie
from .element import Element
from .frame import Frame
from .java_script import JavaScript
from .screenshot import Screenshot
from .select_element import SelectElement
from .table_element import TableElement
from .window import Window


class SeleniumBase(Alert, Browser, Cookie, Element, Frame, JavaScript, Screenshot, SelectElement, TableElement, Window):
    """封装selenium基本操作"""
    pass

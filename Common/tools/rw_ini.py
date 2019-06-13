# 读取配置文件封装

from configparser import ConfigParser


def read_config(config_file_path: str):
    """
    读取配置文件
    :param config_file_path: 文件路径
    :return: 配置文件对象
    """
    rc = ConfigParser()
    rc.read(config_file_path)
    return rc


def write_config(config_file_path: str, secton, option, value=None):
    """
    修改配置文件 ,先读取文件，设置文件，再写入文件
    :param config_file_path:文件路径
    :param secton:目标节点
    :param option:选项
    :param value:值
    :return:
    """
    rc = ConfigParser()
    rc.read(config_file_path)
    rc.set(secton, option, value)
    rc.write(open(config_file_path, 'w', encoding='utf-8'))

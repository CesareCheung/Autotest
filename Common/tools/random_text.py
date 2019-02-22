import threading
import datetime

s = threading.Semaphore(1)
count = 0
now = datetime.datetime.now().strftime("%m%d%H%M")


def get_random_username(n: int, prefix='x') -> list:
    """
    获取随机不重复用户名
    :param n:数量
    :param prefix:前缀
    :return:列表
    """
    s.acquire()  # 获取锁
    global count

    L = []
    for i in range(n):
        L.append(f"{prefix}{now}{count}")
        count += 1

    s.release()  # 释放锁
    return L


s1 = threading.Semaphore(1)

count_phone = 0


def get_random_phone(prefix="133"):
    """
    获取随机手机号码
    :param prefix:前缀
    :return:手机号码
    """
    s1.acquire()
    global count_phone
    phone = (f"{prefix}{now[2:]}{count_phone:02}")
    count_phone += 1
    s1.release()
    return phone

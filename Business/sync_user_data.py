# 用于获取登录业务中，多线程登录

import threading
import time
from Common.tools.read_txt import read_txt


user_data={}
_get_user_s=threading.Semaphore(1)

def acquire_user(file):
    """
    获取用户信息
    :param file:
    :return:
    """
    _get_user_s.acquire()
    try:
        #region 如果文件为空则读取文件
        if len(user_data)==0:
            count=0
            for line in read_txt(file):
                user_data[count]={"user":line,"tag":True}
                count+=1
            if len(user_data)==0:
                raise ValueError(f"文件{file}\t无数据")
        # endregion
        # region 修改获取的状态，确保每次获取的是可用用户，如果不可用则等待
        for i in range(1800):
            for k,v in user_data.items():
                if v.get("tag"):
                    user=v.get("user")
                    user_data[k]['tag']=False
                    return k,user
            time.sleep(2)
        raise TimeoutError("等待用户释放超时:3600s")
        # endregion
    except Exception:
        raise
    finally:
        #不管读取文件是否错误都需要释放
        _get_user_s.release()

_release_user_s=threading.Semaphore(1)



def release_user(k):
    """释放用户信息

    :param k: 编号
    :return:
    """
    _release_user_s.acquire()
    user_data[k]['tag'] = True
    _release_user_s.release()



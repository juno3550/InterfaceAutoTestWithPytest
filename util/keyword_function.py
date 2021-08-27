import hashlib
import traceback
import logging
from util.global_var import *


# 获取递增的唯一数参数
def get_unique_num():
    try:
        with open(UNIQUE_NUM_FILE_PATH, "r+") as f:
            # 先从文件中获取当前的唯一数
            num = f.read()
            # 将唯一数+1再写回文件
            f.seek(0, 0)
            f.write(str(int(num)+1))
        return num
    except:
        logging.error("唯一数文件【%s】读写异常！" % UNIQUE_NUM_FILE_PATH)
        logging.error(traceback.format_exc())
        raise


# MD5加密
def md5(string):
    # 创建一个md5 hash对象
    m = hashlib.md5()
    # 对字符串进行md5加密的更新处理，需要指定编码
    m.update(string.encode("utf-8"))
    # 返回十六进制加密结果
    return m.hexdigest()


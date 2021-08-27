import logging
import logging.handlers
import time
from util.global_var import *


# 日志配置初始化
def log_config_ini():
    # 初始化日志对象
    logger = logging.getLogger()

    # 设置日志级别
    logger.setLevel(logging.INFO)

    # 创建控制台日志处理器
    sh = logging.StreamHandler()

    # 创建文件日志处理器
    # 创建每日的日志文件
    filename_day = PROJECT_ROOT_DIR + "/log/" + "interface_auto_test.%s.log" % time.strftime("%Y-%m-%d")
    fh_day = logging.handlers.TimedRotatingFileHandler(filename_day, when='MIDNIGHT', interval=1, backupCount=3, encoding='utf-8')
    # when: 时间单位， 可选参数
    # interval: 时间间隔
    # backupCount: 日志文件备份数量。 如果backupCount大于0， 那么当生成新的日志文件时，将只保留backupCount个文件， 删除最老的文件。

    # 创建汇总日志文件
    filename_all = PROJECT_ROOT_DIR + "/log/" + "interface_auto_test.log"
    fh_all = logging.handlers.TimedRotatingFileHandler(filename_all, when='MIDNIGHT', interval=1, backupCount=3, encoding='utf-8')

    # 设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh_day.setFormatter(formatter)
    fh_all.setFormatter(formatter)

    # 6、将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh_day)
    logger.addHandler(fh_all)


if __name__ == "__main__":
    logging.info("This is hippop man")


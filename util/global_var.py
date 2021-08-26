import os


# 工程根目录
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 维护唯一数参数的文件路径
UNIQUE_NUM_FILE_PATH = os.path.join(PROJECT_ROOT_DIR, "conf", "unique_num.txt")

# 测试用例文件存放目录
TEST_CASE_DATA_DIR = os.path.join(PROJECT_ROOT_DIR, "test_data", "test_case_data.xlsx")

# 维护一个参数化全局变量：供接口关联使用
PARAM_GLOBAL_DICT = {}

# 日志配置文件路径
LOG_CONF_FILE_PATH = os.path.join(PROJECT_ROOT_DIR, "conf", "logger.conf")

# 测试用例数据列号
API_IP = 2
API_URI = 3
REQUEST_METHOD = 4
API_REQUEST_DATA = 5
RESPONSE_ASSERT_KEYWORD = 6
RESPONSE_EXTRACT_VAR = 7
REQUEST_HEADER = 8
REQUEST_COOKIE = 9


if __name__ == "__main__":
    print(PROJECT_ROOT_DIR)
    print(LOG_CONF_FILE_PATH)
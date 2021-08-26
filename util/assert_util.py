import traceback
import re
from util.log_util import *


# 封装断言功能
def assert_keyword(response, keyword):
    keyword_list = keyword.split("|")
    for keyword in keyword_list:
        try:
            assert keyword.strip() in response.text
            info("【%s】关键字断言成功【%s】" % (keyword, response.text))
        except:
            error("【%s】关键字断言失败【%s】" % (keyword, response.text))
            error(traceback.format_exc())
            raise



import pytest
import allure
import logging
from util.assert_util import assert_keyword
from util.request_util import api_request
from util.global_var import *
from util.excel_util import excel_util


register_test_data = excel_util.get_sheet_data("注册")
login_test_data = excel_util.get_sheet_data("登录")


@allure.feature("登录模块")
@pytest.mark.dependency(name="TestLoginModule")
class TestLoginModule:
        
    @allure.story("注册功能")
    @allure.title('用户注册')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口进行用户注册')  # 添加测试用例描述
    @allure.severity(allure.severity_level.BLOCKER)  # 阻塞级别
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('case_data', register_test_data)
    def test_register(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("登录功能")
    @allure.title('用户登录')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口进行用户登录')  # 添加测试用例描述
    @allure.severity(allure.severity_level.BLOCKER)  # 阻塞级别
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('case_data', login_test_data)
    def test_login(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])


if __name__ == "__main__":
    test_dir = os.path.dirname(__file__)
    pytest.main(['-s', '-q', test_dir, '--alluredir', '../test_result/', "--clean-alluredir"])
    os.system('allure generate ../test_result/ -o ../test_report/ --clean')
    os.system('allure open -h 127.0.0.1 -p 8881 ../test_report/')
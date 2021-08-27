import pytest
import allure
import logging
from util.assert_util import assert_keyword
from util.request_util import api_request
from util.global_var import *
from util.excel_util import excel_util


create_test_data = excel_util.get_sheet_data("创建博文")
user_blog_search_test_data = excel_util.get_sheet_data("查看用户博文")
blog_content_test_data = excel_util.get_sheet_data("查看博文内容")
blog_update_test_data = excel_util.get_sheet_data("更新博文内容")
blog_batch_search_test_data = excel_util.get_sheet_data("批量查询博文")
delete_test_data = excel_util.get_sheet_data("删除博文")


@allure.feature("编辑模块")
@pytest.mark.dependency(name="TestEditModule", depends=["TestLoginModule"], scope='package')
class TestEditModule:

    # def setup_class(self):
    #     初始化调用注册和登录接口，获取userid和token供后续接口关联
    #     使用该初始化则可不依赖test_login_module.py的TestLoginModule
    #     get_userid_and_token()

    @allure.story("博文创建功能")
    @allure.title('创建博文')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口创建博文')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 阻塞级别
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('case_data', create_test_data)
    def test_create(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("用户博文查询功能")
    @allure.title('查看用户博文')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口查看用户所有博文')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 严重级别
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('case_data', user_blog_search_test_data)
    def test_user_blog_search(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("博文内容查询功能")
    @allure.title('查看博文内容')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口查看博文内容')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 严重级别
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('case_data', blog_content_test_data)
    def test_blog_content_search(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("博文内容更新功能")
    @allure.title('更新博文内容')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口更新博文内容')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 严重级别
    @pytest.mark.run(order=6)
    @pytest.mark.parametrize('case_data', blog_update_test_data)
    def test_blog_content_update(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("批量查询博文功能")
    @allure.title('批量查询博文')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口批量查询博文')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 严重级别
    @pytest.mark.run(order=7)
    @pytest.mark.parametrize('case_data', blog_batch_search_test_data)
    def test_blog_batch_search(self, case_data):
        with allure.step("读取请求数据，调用接口"):
            logging.info("接口用例数据：%s" % case_data)
            response = api_request(case_data[API_IP], case_data[API_URI], case_data[REQUEST_METHOD],
                                   case_data[API_REQUEST_DATA], case_data[RESPONSE_EXTRACT_VAR],
                                   case_data[REQUEST_HEADER], case_data[REQUEST_COOKIE])
        with allure.step("获取响应数据，进行断言"):
            assert_keyword(response, case_data[RESPONSE_ASSERT_KEYWORD])

    @allure.story("博文删除功能")
    @allure.title('删除博文')  # 指定测试用例标题，默认是函数名
    @allure.description('通过接口删除博文')  # 添加测试用例描述
    @allure.severity(allure.severity_level.CRITICAL)  # 严重级别
    @pytest.mark.run(order=8)
    @pytest.mark.parametrize('case_data', delete_test_data)
    def test_delete(self, case_data):
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
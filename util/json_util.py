import json
import traceback
import logging


# JSON 处理功能
class JsonHandler:

    # 将json串转成字典对象
    @staticmethod
    def json_to_dict(json_str):
        try:
            return json.loads(json_str, encoding="utf-8")
        except:
            logging.error("Json串转换字典对象 失败：【%s】" % json_str)
            logging.error(traceback.format_exc())
            raise

    # 将字典对象转成json串
    @staticmethod
    def dict_to_json(dict_obj):
        try:
            return json.dumps(dict_obj, ensure_ascii=False)
        except:
            logging.error("字典对象转换Json串 失败：【%s】" % dict_obj)
            logging.error(traceback.format_exc())
            raise

    # 在字典中根据key找到value值（默认找第一个值）
    @staticmethod
    def find_value(response, key):
        if isinstance(response, str):
            response = JsonHandler.json_to_dict(response)
        if not isinstance(response, dict):
            logging.error("【%s】非字典类型，在响应数据中查找值失败！" % response)
            raise
        for k, v in response.items():
            if k == key:
                return v
            elif isinstance(v, dict):
                return JsonHandler.find_value(v, key)
            elif isinstance(v, list):
                for value in v:
                    if isinstance(value, dict):
                        return JsonHandler.find_value(value, key)
        else:
            logging.error("键【%s】在响应数据中不存在【%s】！" % (key, response))
            raise


if __name__ == "__main__":
    rsp_str = '{"data": [{"update_time": null, "title": "title test", "content": "content test", "articleId": 128, "owner": 310, "posted_on": "2021-08-25 21:09:01"}], "code": "00", "userid": 310}'
    print(JsonHandler.find_value(rsp_str, "articleId"))

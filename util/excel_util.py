import xlrd
import traceback
import logging
from util.global_var import *


class ExcelUtil:

	# Excel文件初始化
	def __init__(self, file_name):
		try:
			self.wb = xlrd.open_workbook(file_name)
		except:
			logging.error("Excel初始化失败：【%s】" % file_name)
			logging.error(traceback.format_exc())
			raise

	# 根据sheet名获取所有行的用例数据
	def get_sheet_data(self, sheet_name):
		try:
			self.sheet = self.wb.sheet_by_name(sheet_name)
		except:
			logging.error("Sheet测试数据读取失败：【%s】" % sheet_name)
			logging.error(traceback.format_exc())
			raise
		else:
			result = []
			for row_index in range(1, self.sheet.nrows):  # 去除标题行
				result.append(self.sheet.row_values(row_index))
			if len(result) < 1:
				logging.info("【%s】测试数据为空，无需执行" % sheet_name)
			return result


excel_util = ExcelUtil(TEST_CASE_DATA_DIR)


if __name__ == "__main__":
	print(excel_util.get_sheet_data("用例名称"))
# 读取Excel文件中的用例

"""
功能需求：获取excel文件指定数据
入参：
    ---1 文件路径（路径+文件名+文件格式）
    ---2 读取指定的表
    ---3 读取指定的数据

出参：函数使用者需要什么就处理成什么
    ---返回数据是什么
        ---请求体
        ---预期结果
        ---...
    ---返回数据的类型
        ---元组
        ---字典
        ---列表
        ---字符串
        ---集合
"""

import xlrd
import json


def get_execl_data(file_path, sheet_name, case_name):
    # 存放结果
    res_list = []
    # 文件在磁盘---读取到---内存
    # formatting_info=True---保持表格原样式，一定要加
    work_book = xlrd.open_workbook(file_path, formatting_info=True)
    # 获取所有的表名
    # print(work_book.sheet_names())
    # 选中对应的表
    work_sheet = work_book.sheet_by_name(sheet_name)
    # 获取第一行数据
    # print(work_sheet.row_values(0))
    # 获取第二列数据
    # print(work_sheet.col_values(1))

    # 获取单元格数据
    # print(work_sheet.cell(0, 0).value)

    # 获取需要的数据
    # 要把空行过滤掉
    row_index = 0
    for one in work_sheet.col_values(1):
        if case_name in one:
            row_index += 1
            req_body = work_sheet.cell(row_index, 6).value
            exp_data = work_sheet.cell(row_index, 7).value
            # res_list.append((req_body, exp_data))
            # 把读取到的字符串格式转化为字典格式
            res_list.append((json.loads(req_body), json.loads(exp_data)))
    return res_list


"""
优化点：
---列下标是写死的，要修改只能改代码
---单元格数据不一定是Json，有些不能转化为字典
---不能获取其他多列数据
---如何定制化执行部分模块代码
"""


# if __name__ == '__main__':
#     res = get_execl_data('../data/my_data.xls', 'Sheet1', 'login')
#     print(res)


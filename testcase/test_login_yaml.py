import pytest
from libs.Login import Login
from tools.handle_yaml import get_yaml_data
import data
import allure
import os
# yaml用例调用


class TestLoginNew:
    @pytest.mark.parametrize('inData,expData', get_yaml_data('../data/loginCase.yaml'))
    def test_login_new(self, inData, expData):
        res = Login().login(inData)
        assert res['code'] == expData['code']


# if __name__ == '__main__':
#     pytest.main(["test_login_yaml.py", "-s", "--alluredir", "../report/tmp"])
#     # os.system("allure serve ../report/tmp")
#     """
#     allure报告方案原理：
#         ---生成报告所需文件
#         ---使用组件打开可视化报告
#     """

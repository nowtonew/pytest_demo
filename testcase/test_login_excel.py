from libs.Login import Login
from tools.handle_excel import get_execl_data
import data
import pytest
import allure
import os
# excel用例调用


class TestLogin:
    # 测试接口
    # 数据驱动
    @pytest.mark.login
    @pytest.mark.parametrize('req_body, exp_data', get_execl_data('../data/my_data.xls', 'login', 'login'))
    def test_login(self, req_body, exp_data):
        # 登陆接口所有用例
        res = Login().login(req_body)
        assert res['code'] == exp_data['code']

    @pytest.mark.logout
    @pytest.mark.parametrize('req_body, exp_data', get_execl_data('../data/my_data.xls', 'logout', 'logout'))
    def test_logout(self, req_body, exp_data):
        # 登出接口所有用例
        res = Login().logout(req_body)
        assert res['code'] == exp_data['code']


# if __name__ == '__main__':
#     print('---test result---')
#     os.system("rm -rf ../report/tmp/")  # 清除之前的报告数据
#     pytest.main([__file__, '-s', '--alluredir', '../report/tmp'])
#     os.system("allure serve ../report/tmp")
#     # -s 打印输出




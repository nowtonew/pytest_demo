# 自动化测试前的环境初始化操作
# 自动化测试后数据清除操作
# 文件名一定不能改，而且只能叫这个名字
import os

import pytest


@pytest.fixture(scope='session', autouse=True)
def start_running():
    print('----------Start Auto API Test----------')
    yield
    print('----------Finish Test Clean Data----------')

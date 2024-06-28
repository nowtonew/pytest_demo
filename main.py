import pytest
import os
import allure


# os.system("rm -rf output/report")  # 清除之前的报告数据
pytest.main([ '-m login', '--alluredir=output/report', '--clean-alluredir'])
os.system("allure serve output/report")
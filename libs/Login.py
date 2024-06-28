"""
封装代码：使用函数还是类？
用类：封装、多态、继承
因为我们需要类的这些特性
"""
# 封装 登陆模块 命名规范：首字母大写，使用驼峰法
from configs.config import HOST
from tools.handle_data import get_md5_data
import requests
import pprint


class Login:
    # 封装---登陆接口
    def login(self, body_data):
        # 请求的url
        url = f'{HOST}/login-or-register/do?_=1718216550908'
        # 请求方法可以不用写，request会调
        # 请求头可以不写
        # 请求体
        body_data['password'] = get_md5_data(body_data['password'])
        payload = body_data
        """
        data：使用场景---请求头中Content-Type字段值为表单格式时
        ---表单格式 form a=1&b=2
        ---表单里面有json a=1&b={"name":"xt"}
        json：使用场景---请求头中，Content-Type字段值为json格式时
        
        ---登陆接口的密码使用了什么加密操作？
            ---MD5
                ---简单的MD5
                ---MD5加盐
                ---MD5加双重盐
            ---RSA非堆称加密 公密钥
            ---AES
        """
        resp = requests.post(url, json=payload)

        # 打印响应数据，以字符串类型（返回是双引号）
        # return resp.text

        # 打印响应数据，以字典类型（返回是单引号，字典格式）
        return resp.json()

    def logout(self, body_data):
        url = f"{HOST}/logout/do?_=1718216550908"
        resp = requests.post(url, json=body_data)
        return resp.json()


# if __name__ == '__main__':
#     test_data_in = {"account": 15502905952, "password": "yj980214"}
#     test_data_out = {"account": 15502905952}
#     # 1.使用类去创建实例
#     # 有两步：__new__(self) ; __init__(self)
#     login = Login()
#     # 2.调用登陆接口
#     res_login = login.login(test_data_in)
#     res_logout = login.logout(test_data_out)
#     print(res_login, '\n', res_logout)

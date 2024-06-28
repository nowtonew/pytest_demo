# 处理加密

"""
函数需求： MD5加密操作
入参：明文---string
出参：加密的密文---string
"""

import hashlib


def get_md5_data(pwd: str):
    # 实例化MD5对象
    md5 = hashlib.md5()
    # 调用加密操作
    md5.update(pwd.encode('utf-8'))
    # 返回加密后的结果
    return md5.hexdigest()
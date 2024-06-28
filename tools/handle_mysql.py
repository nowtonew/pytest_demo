# 导入数据库
import pymysql

# 创建连接：host user pwd port database code
pymysql.connect(host='127.0.0.1', port=3306, user='root', password='980214', database='testcase', charset='utf8')

# -*- coding:utf-8 -*-
"""
作者:13451
日期:2024年07月03日
"""
from vanna.ollama import Ollama
from vanna.chromadb import ChromaDB_VectorStore
import pandas as pd
import mysql.connector
from vanna.flask import VannaFlaskApp
############USING THE OLLAMA#####################
class MyVanna(ChromaDB_VectorStore, Ollama):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        Ollama.__init__(self, config=config)

# vn = MyVanna(config={'model': 'mistral'})

vn = MyVanna(config={'model': 'llama3'})
############USING THE OLLAMA#####################


# # 尝试连接到 MySQL 数据库
# try:
#     vn.connect_to_mysql(host='localhost', dbname='test1', user='root', password='123456', port=3306)
#     print("成功连接到数据库")
# except Exception as e:
#     print(f"连接数据库失败: {e}")
#     raise
#
# # 执行简单查询以检查连接是否成功
# try:
#     result = vn.run_sql("SHOW TABLES;")
#     print("数据库连接成功，以下是数据库中的表:")
#     print(result)
# except Exception as e:
#     print(f"执行查询失败: {e}")

# vn.connect_to_mysql(host='192.168.0.115', dbname='ichatdev', user='admin', password='cF123?456Cf', port=3306)
vn.connect_to_mysql(host='localhost', dbname='test1', user='root', password='123456', port=3306)


# vn.train(question='目前有哪些书？', sql='SELECT * FROM book')

# vn.train(ddl="""
#     CREATE TABLE IF NOT EXISTS book (
#         id int NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '表唯一ID',
#         create_time datetime NULL DEFAULT NULL COMMENT '创建时间',
#         book_name varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '书的名字',
#         book_code varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '书的编号',
#         book_introduction varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '书的简介',
#         book_publisher varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL COMMENT '书的出版社',
#     )CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = 'book表';
# """)
# training_data = vn.get_training_data()
# training_data

# vn.ask(question="每种书各有多少本？")

app = VannaFlaskApp(vn)
app.run()

# def run_sql(sql: str) -> pd.DataFrame:
#     cnx = mysql.connector.connect(user='root', password='123456', host='localhost', database='test1')
#     cursor = cnx.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     columns = cursor.column_names
#     # print('columns:',columns)
#     df = pd.DataFrame(result, columns=columns)
#     # print(df)
#     return df
#
#
# # 将函数设置到vn.run_sql中
# vn.run_sql = run_sql
# # print(run_sql)
# vn.run_sql_is_set = True
# print(vn.get_training_data())

# 获取所有训练数据
# training_data = vn.get_training_data()
#
# # 遍历所有训练数据的 ID 并逐个删除
# for training_id in training_data['id']:
#     vn.remove_training_data(id=training_id)

# vn.remove_training_data(id="ff076ca2-df1a-5fbe-b32a-61cfde096669-ddl")
# vn.ask(question="SHOW TABLES;")


###########这个一定可以连接成功determine connect----------------------
# import mysql.connector
#
# db_config = {
#     'user': 'root',
#     'password': '123456',
#     'host': 'localhost',
#     'database': 'test1'
# }
#
# # 建立数据库连接
# conn = mysql.connector.connect(**db_config)
# cursor = conn.cursor()
# # query = "SELECT * FROM common_phrases LIMIT 10"  # 示例查询语句，查询表中的前10条记录
# query = "SHOW TABLES"
#
# cursor.execute(query)
#
# # 获取查询结果
# results = cursor.fetchall()
#
# # 打印查询结果
# for row in results:
#     print(row)
#
# # 关闭游标和连接
# cursor.close()
# conn.close()



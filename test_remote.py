from vanna.flask import VannaFlaskApp
import pandas as pd
import mysql.connector
import vanna
from vanna.remote import VannaDefault

api_key = '209814156b194a7e9df7eafb01fdb16b'
vanna_model_name = 'lyh1'
vn = VannaDefault(model=vanna_model_name, api_key=api_key)

vn.connect_to_mysql(host='localhost', dbname='test1', user='root', password='123456', port=3306)


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

# vn.train(question='年龄最大的是哪个？',sql='SELECT name FROM customer ORDER BY age DESC LIMIT 1')
# vn.train(question='居住在重庆的人有哪些？',sql="SELECT name FROM customer WHERE residential_city LIKE '%重庆%'")


# first_conversation_sql = vn.ask('居住在重庆的人有哪些？')
# print(type(first_conversation_sql))

app = VannaFlaskApp(vn)
app.run()


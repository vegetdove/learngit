# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
#   （表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；
#    数据库操作需要加入异常处理逻辑；

import pymysql

db = pymysql.connect("localhost","root","0414666jy","test")

cursor = db.cursor()

#创建表
sql_create = "create table board(ID varchar(10),topic varchar(100),name varchar(20),time varchar(20),delete_state varchar(1))"
try:
    cursor.execute(sql_create)
    db.commit()
except Exception as e :
    print("出现数据库异常：",e)

#增
sql_append = "insert into board(ID,topic,name,time,delete_state) values(%s,%s,%s,%s,%s)"
try:
    cursor.execute(sql_append, ("101", "love", "Bob", "2020.01.01","0"))
    cursor.execute(sql_append, ("102", "friendship", "Jack", "2018.02.01","0"))
    cursor.execute(sql_append, ("103", "war", "Tom", "2019.05.04","0"))
    cursor.execute(sql_append, ("104", "food", "Black", "2020.03.01","0"))
    db.commit()
except Exception as e :
    print("出现数据库异常：",e)

#删
sql_delete = "update board set delete_state = 1 where ID = %s" % ("102")
try:
    cursor.execute(sql_delete)
    db.commit()
except Exception as e :
    print("出现数据库异常：",e)

#改
sql_update = "update board set ID = ID + 1 where name = '%s'" % ('Black')
try:
    cursor.execute(sql_update)
    db.commit()
except Exception as e :
    print("出现数据库异常：",e)

#查
sql_search = "select * from board"
try:
    cursor.execute(sql_search)
    result = cursor.fetchall()
    for x in result :
        print(x)
    db.commit()
except Exception as e :
    print("出现数据库异常：",e)

db.close()
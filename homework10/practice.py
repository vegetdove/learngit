# 练习二：
#    创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；
#    完成对这个表记录的增，删，改，查询；
#    用PyMySQL驱动方式

import pymysql


db = pymysql.connect("localhost","root","0414666jy","test")

cursor = db.cursor()

cursor.execute("create table board(ID varchar(10),topic varchar(100),name varchar(20),time varchar(20))")

#增
cursor.execute("insert into board(ID,topic,name,time) values(%s,%s,%s,%s)",("101","love","Bob","2020.01.01"))
cursor.execute("insert into board(ID,topic,name,time) values(%s,%s,%s,%s)",("102","friendship","Jack","2018.02.01"))
cursor.execute("insert into board(ID,topic,name,time) values(%s,%s,%s,%s)",("103","war","Tom","2019.05.04"))
cursor.execute("insert into board(ID,topic,name,time) values(%s,%s,%s,%s)",("104","food","Black","2020.03.01"))

#删
sql = "delete from board where ID = %s" % ("102")
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

#改
sql = "update board set ID = ID + 1 where name = '%s'" % ('Bob')
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

#查
cursor.execute("select * from board")
result = cursor.fetchall()
for x in result :
    print(x)

db.close()
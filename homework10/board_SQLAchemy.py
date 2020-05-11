# 3  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
#    使用SQLAchemy 驱动模块，实现对这个表的增加，删除，修改，查询；

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Board(Base):
    __tablename__ = 'board'
    ID = Column(String(10), primary_key=True)
    topic = Column(String(100))
    name = Column(String(20))
    time = Column(String(20))
    delete_state = Column(String(1))

engine = create_engine('mysql+mysqlconnector://root:0414666jy@localhost:3306/test')

DBSession = sessionmaker(bind=engine)


# 增
try:
    session = DBSession()
    new_record0 = Board(ID = "101", topic = "love", name = "Bob", time = "2020.01.01", delete_state = "0")
    new_record1 = Board(ID = "102", topic = "friendship", name = "Jack", time = "2018.02.01", delete_state = "0")
    new_record2 = Board(ID = "103", topic = "war", name = "Tom", time = "2019.05.04", delete_state = "0")
    new_record3 = Board(ID = "104", topic = "food", name = "Black", time = "2020.03.01", delete_state = "0")
    session.add(new_record0)
    session.add(new_record1)
    session.add(new_record2)
    session.add(new_record3)
    session.commit()
    session.close()
except Exception as e :
    print("出现数据库异常：",e)


# 查
try:
    session = DBSession()
    record = session.query(Board).filter(Board.name=='Tom').one()
    print("查找的记录为：")
    print('ID:{0}'.format(record.ID))
    print('topic:{0}'.format(record.topic))
    print('name:{0}'.format(record.name))
    print('time:{0}'.format(record.time))
    print('delete_state:{0}'.format(record.delete_state))
    session.close()
except Exception as e :
    print("出现数据库异常：",e)


# 改
try:
    session = DBSession()
    record = session.query(Board).filter_by(ID='102').first()
    record.name = "Jenny"
    session.commit()
    session.close()
except Exception as e :
    print("出现数据库异常：",e)


# 删
try:
    session = DBSession()
    record = session.query(Board).filter_by(ID='104').first()
    record.delete_state = "1" #用修改delete_state的方式表示删除
    session.commit()
    session.close()
except Exception as e :
    print("出现数据库异常：",e)
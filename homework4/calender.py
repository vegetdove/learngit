# 2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，
# 能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）


import datetime,time

def get_weekday(date):
    weekday_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
  }
    day = date.weekday()
    return weekday_dict[day]

def get_week_num(date) :
    year = date.year
    timedet = int((date-datetime.date(year,1,1)).days/7) + 1
    return timedet
 
def get_week_nums(date) :
    year = date.year
    timedet = int((date-datetime.date(year,2,17)).days/7) + 1
    return timedet

if __name__ == "__main__":
    print(get_weekday(datetime.date(2018,4,3)))
    print("第",get_week_num(datetime.date(2018,4,3)),"周")
    print("校历第",get_week_nums(datetime.date(2018,4,3)),"周")
    pass
import time

# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(time.strftime('%Y%m%d'))

from datetime import datetime, timedelta

# print(datetime.datetime.now())
# new_time = datetime.timedelta(minutes=10)
# print(datetime.datetime.now() + new_time)
# 
# one_day = datetime.datetime(2008, 5, 27)
# new_date = datetime.timedelta(days=10)
# print(one_day + new_date)

end_time = datetime.now()
start = end_time - timedelta(minutes=30)
str_format = "%d月%d日-%02d:%02d-%02d:%02d" % (
    end_time.month, end_time.day, end_time.hour, end_time.minute, start.hour, start.minute)
print(str_format)

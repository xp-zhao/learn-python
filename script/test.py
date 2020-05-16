import uuid
import requests
import json
import time

# 从文件中读取 Cookie
path = "E:\\fiddler\\data\\cookie.txt"
_cookie = None
_st = None
_tk = None
depaCode = 5101070042
with open(path, 'r', encoding='utf-8') as file_object:
    lines = file_object.readlines()
    _cookie = lines[0].strip('\n')
    _st = lines[1].strip('\n')
    _tk = lines[2].strip('\n')

headers = {
    "Accept": "application/json, text/plain, */*",
    "st": _st,
    "tk": _tk,
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; MI 6X Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045223 Mobile Safari/537.36 MMWEBID/8833 MicroMessenger/7.0.14.1660(0x27000E37) Process/tools NetType/4G Language/zh_CN ABI/arm64 WeChat/arm64",
    "Sec-Fetch-Mode": "cors",
    "X-Requested-With": "com.tencent.mm",
    "Sec-Fetch-Site": "same-origin",
    "Referer": "https://wx.healthych.com/index.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cookie": _cookie
}
# get 请求
url = "https://wx.healthych.com"
# 用户信息
user_path = "/order/linkman/findByUserId.do?userId=4344181"
# 日期
date_range_path = "/order/subscribe/workDays.do"
date_range_data = {
    "depaCode": depaCode,
    "linkmanId": 2944438,
    "vaccCode": 8803,
    "vaccIndex": 1,
    "departmentVaccineId": 5885
}

date_rep = requests.get(url + date_range_path, date_range_data, verify=False, headers=headers)
date_obj = json.loads(date_rep.text)
print(date_rep.json())
first_date = date_obj['data']['dateList'][0]
print("日期: %s" % first_date)
# 时间
time_range_path = "/order/subscribe/departmentWorkTimes2.do"
time_range_data = {
    "depaCode": depaCode,
    "linkmanId": 2944438,
    "vaccCode": 8803,
    "vaccIndex": 1,
    "departmentVaccineId": 5885,
    "subsribeDate": first_date
}
time_rep = requests.get(url + time_range_path, time_range_data, verify=False, headers=headers)
time_obj = json.loads(time_rep.text)
print(time_obj)
time_list = time_obj['data']['times']['data']
first_time = time_obj['data']['times']['data'][1]['id']
for t in time_list:
    if t['maxSub'] > 0:
        first_time = t['id']
        break
print("时间: %s" % first_time)

# 下单
order_path = "/order/subscribe/add.do"
str_random = str(uuid.uuid1()).replace("-", '')
order_data = {
    "vaccineCode": 8803,
    "vaccineIndex": 1,
    "linkmanId": 2944438,
    "subscribeDate": first_date,
    "subscirbeTime": first_time,
    "departmentVaccineId": 5885,
    "depaCode": str(depaCode) + "_" + str_random,
    "serviceFee": 0
}

order_rep = requests.get(url + order_path, order_data, verify=False, headers=headers)
obj = json.loads(order_rep.text)
while not obj['ok']:
    time.sleep(1)
    order_rep = requests.get(url + order_path, order_data, verify=False, headers=headers)
    obj = json.loads(order_rep.text)
    print(order_rep.json())
print(order_rep.json())

from urllib import request
from urllib import parse
import socket
import urllib

# url = "http://www.baidu.com"
# response = request.urlopen(url, timeout=10)
# print(response.read().decode('utf-8'))

# get 请求
try:
    response1 = request.urlopen("http://httpbin.org/get", timeout=1)
    print(response1.read())
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("time out")

# post 请求
# data = bytes(parse.urlencode({"world": "hello"}), encoding='utf-8')
# response2 = request.urlopen("http://httpbin.org/post", data=data)
# print(response2.read().decode('utf-8'))

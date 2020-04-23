import requests

# get 请求
url = "http://httpbin.org/get"
data = {"key": "value", "abc": "xyz"}
# response = requests.get(url, data)
# print(response.text)

post_url = "http://httpbin.org/post"
response = requests.post(post_url, data)
print(response.json())

import requests
import re

content = requests.get("http://www.cnu.cc/discoveryPage/hot-人像").text
# print(content)

# <div class="grid-item work-thumbnail">
# <a href="http://www.cnu.cc/works/379558" class="thumbnail" target="_blank">
# <div class="title">解脱</div>
# <div class="author">伟嘉不猫梁</div>

# <div class="grid-item work-thumbnail">
# <a href="(.*?)".*?title">(.*?)</div>
# <div class="author">伟嘉不猫梁</div>

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)
for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))

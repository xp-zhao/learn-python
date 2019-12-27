import datetime
from urllib import parse

import requests
from bs4 import BeautifulSoup as BS


def answer_list(choice):
    length = len(choice)
    if length == 2:
        return {'A': choice[0], 'B': choice[1]}
    if length == 3:
        return {'A': choice[0], 'B': choice[1], 'C': choice[2]}
    if length == 4:
        return {'A': choice[0], 'B': choice[1], 'C': choice[2], 'D': choice[3]}


def search(question, choice):
    pagenum = [0, 10, 20]
    answer = []
    startTime = datetime.datetime.now()
    for i in pagenum:
        q = parse.quote(question.encode('gbk'))
        url = 'https://zhidao.baidu.com/search?word=' + q \
              + '&ie=gbk&site=-1&sites=0&date=0&pn=' + str(i)
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, verify=False)
        r.encoding = 'gbk'
        soup = BS(r.text, 'html.parser')
        want = soup.find('div', id='wgt-list')
        wants = want.find_all('dl', class_='dl')
        for i in wants:
            ans = i.find('dd', class_='dd answer').text
            answer.append(ans)
    endTime = datetime.datetime.now()
    print((endTime - startTime).seconds)
    choice_set = answer_list(choice)
    # 计算四个选项在爬取百度答案中的出现次数
    results = {}
    for i in choice_set:
        account = []
        for j in answer:
            if choice_set[i] in j:
                account.append(j)
        result = len(account) / 30
        results[i] = result
        print((i + ' : %.2f%%' % (result * 100)).center(50, '-'))

    # 选出数值最大元素的对应键
    bestchoice = max(results.items(), key=lambda x: x[1])[0]
    print(('此题最好选' + bestchoice).center(50, '-') + '\n\n\n')
    endTime1 = datetime.datetime.now()
    print((endTime1 - endTime).seconds)


if __name__ == '__main__':
    search("豪猪和一下哪种动物是近亲？", ["老鼠", "猪"])
    search("内蒙古自治区的省会是？", ["乌鲁木齐", "齐齐哈尔", "呼和浩特", "呼伦贝尔"])

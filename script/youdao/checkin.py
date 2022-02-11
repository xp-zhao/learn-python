import hashlib
import json
import os
import time

import requests
import urllib3

urllib3.disable_warnings()

# 配置各种key
pushplus_token = 'token'


def pushplus(content: str, title='有道云笔记签到'):
    #在pushplus网站中可以找到
    url = 'http://www.pushplus.plus/send?token=' + pushplus_token + '&title=' + title + '&content=' + content
    requests.get(url)


def checkin():
    username = '账号'
    password = '密码'

    login_url = 'https://note.youdao.com/login/acc/urs/verify/check?app=web&product=YNOTE&tp=urstoken&cf=6&fr=1&systemName=&deviceType=&ru=https%3A%2F%2Fnote.youdao.com%2FsignIn%2F%2FloginCallback.html&er=https%3A%2F%2Fnote.youdao.com%2FsignIn%2F%2FloginCallback.html&vcode=&systemName=mac&deviceType=MacPC&timestamp=1611466345699'
    checkin_url = 'http://note.youdao.com/yws/mapi/user?method=checkin'

    parame = {
        'username': username,
        'password': hashlib.md5(password.encode('utf8')).hexdigest(),
    }

    s = requests.Session()

    try:
        # 登录
        s.post(url=login_url, data=parame, verify=False)

        # 签到
        r = s.post(url=checkin_url)
    except:
        pushplus('签到失败')
        exit()
    if r.status_code == 200:
        info = json.loads(r.text)
        total = info['total'] / 1048576
        space = info['space'] / 1048576
        t = time.strftime('%Y-%m-%d %H:%M:%S',
                          time.localtime(info['time'] / 1000))
        pushplus('{} | 这次签到获得：{} M | 总共获得：{} M | 签到时间：{}'.format(
            username, space, total, t))


if __name__ == "__main__":
    checkin()

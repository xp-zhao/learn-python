import json
import time

import requests

base_url = 'https://juejin-game.bytedance.com/game/'
juejin_base_url = 'https://juejin.cn'


def game_info(token: str):
    url = 'sea-gold/home/info'
    r = requests.get(base_url + url, {
        'uid': '1521379822807480',
        'time': time.time()
    },
                     headers={
                         'referer': 'https://juejin.cn/',
                         'authorization': 'Bearer ' + token
                     })
    return r.json()


def get_token() -> str:
    cookie = '_ga=GA1.2.1446831616.1639098104; MONITOR_WEB_ID=ff41dcde-9afb-45d2-bb33-2b0f05d05f02; n_mh=NREEbu-n6wH3bBIaB_fvQmLwu-QfGLw94B9FBDwDcbE; __tea_cookie_tokens_2608=%7B%22user_unique_id%22%3A%226935610926884259364%22%2C%22web_id%22%3A%226935610926884259364%22%2C%22timestamp%22%3A1640826239154%7D; passport_csrf_token_default=f4d8c3835ef613537d1aac0d550360b3; passport_csrf_token=f4d8c3835ef613537d1aac0d550360b3; sid_guard=9114fbeed52f51626d32216a95958e65|1644314186|5184000|Sat,+09-Apr-2022+09:56:26+GMT; uid_tt=4054a5a0e8d71cc882cd7d1407a41d8b; uid_tt_ss=4054a5a0e8d71cc882cd7d1407a41d8b; sid_tt=9114fbeed52f51626d32216a95958e65; sessionid=9114fbeed52f51626d32216a95958e65; sessionid_ss=9114fbeed52f51626d32216a95958e65; sid_ucp_v1=1.0.0-KGEyNzViZGFlNWEyZDQ4NzVlMjMzNTBhZDc0MGZiNmUzMDJhZDExZmQKFgi406C__fXZAhDK_IiQBhiwFDgIQAsaAmxmIiA5MTE0ZmJlZWQ1MmY1MTYyNmQzMjIxNmE5NTk1OGU2NQ; ssid_ucp_v1=1.0.0-KGEyNzViZGFlNWEyZDQ4NzVlMjMzNTBhZDc0MGZiNmUzMDJhZDExZmQKFgi406C__fXZAhDK_IiQBhiwFDgIQAsaAmxmIiA5MTE0ZmJlZWQ1MmY1MTYyNmQzMjIxNmE5NTk1OGU2NQ; _gid=GA1.2.2124310128.1644908998; _tea_utm_cache_2608={"utm_medium":"user_center","utm_campaign":"hdjjgame"}'
    r = requests.get('https://juejin.cn/get/token', headers={'cookie': cookie})
    return json.loads(r.text)['data']

token = get_token()
game = game_info(token)
data = game['data']
game_data = data['gameInfo']
user_info = data['userInfo']
map_data = game_data['mapData']
block_data = game_data['blockData']
cur_pos = game_data['curPos']
print(map_data)
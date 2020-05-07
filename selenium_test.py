import os
import sys
from datetime import datetime, timedelta
from time import time, sleep

import pyautogui as gui
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from clipboard import clipboard as clip


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS',
                        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


chrome_driver = resource_path('chromedriver.exe')
# chrome_driver = 'chromedriver.exe'
chrome_options = Options()
# 设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1920,780")

#  解决“chrome正受到自动测试软件的控制”信息栏显示，使用disable-infobars属性不生效问题
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
driver.get(
        'http://10.25.150.103:19095/d/Kz4-4g6Wk/guan-jian-zhi-biao-zhan-shi-tu?orgId=1&from=now-3h&to=now&refresh=5s')
sleep(2)

driver.maximize_window()
# driver.find_element_by_id('kw').send_keys('当前时间')
# driver.find_element_by_id('su').click()
driver.find_element_by_name('user').send_keys('')
driver.find_element_by_name('password').send_keys('')
sleep(2)
driver.find_element_by_xpath("//button[@type='submit']").click()

sleep(5)


def sent_msg():
    # 从剪切板中获取内容
    gui.hotkey('ctrl', 'v')
    # 发送内容
    gui.hotkey('enter')


def get_cur_time():
    unit = 1800
    cur_time = int(datetime.now().timestamp())
    hour_stamp = cur_time - (cur_time % unit)
    return datetime.fromtimestamp(hour_stamp)


def get_text():
    end_time = get_cur_time()
    start = end_time - timedelta(minutes=30)
    str_format = "%d月%d日 %02d:%02d-%02d:%02d" % (
        end_time.month, end_time.day, start.hour, start.minute,
        end_time.hour, end_time.minute)
    result = "客户端后台系统 %s 系统运行正常" % str_format
    return result


def send_screenshot():
    # 截取当前窗口，并指定截图图片的保存位置
    path = "screen_img.png"
    # 刷新
    driver.refresh()
    # 全屏
    driver.maximize_window()
    sleep(2)
    driver.get_screenshot_as_file(path)
    print("保存截图")
    clip.setText(get_text())
    sent_msg()
    sleep(1)
    clip.setImage(path)
    sent_msg()


schedule.every(30).minutes.do(send_screenshot)

stop_time = datetime(2020, 5, 9, 9, 20, 00)
start_time = datetime(2020, 4, 30, 21, 30, 00)
print("开始截图")
send_screenshot()
while True:
    cur_time = datetime.now()
    if cur_time.__ge__(stop_time):
        break
    if cur_time.__le__(start_time):
        continue
    schedule.run_pending()
    sleep(1)
print("程序结束")
driver.quit()

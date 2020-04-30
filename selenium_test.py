from datetime import datetime, timedelta
from time import sleep

import pyautogui as gui
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from clipboard import clipboard as clip

chrome_driver = 'chromedriver.exe'
chrome_options = Options()
# 设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=4000,1600")

#  解决“chrome正受到自动测试软件的控制”信息栏显示，使用disable-infobars属性不生效问题
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
driver.get('https://www.baidu.com')

driver.maximize_window()
driver.find_element_by_id('kw').send_keys('当前时间')
driver.find_element_by_id('su').click()
sleep(2)


def sent_msg():
    # 从剪切板中获取内容
    gui.hotkey('ctrl', 'v')
    # 发送内容
    gui.hotkey('enter')


def get_text():
    end_time = datetime.now()
    start = end_time - timedelta(minutes=30)
    str_format = "%d月%d日-%02d:%02d-%02d:%02d" % (
        end_time.month, end_time.day, end_time.hour, end_time.minute, start.hour, start.minute)
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
    clip.setImage(path)
    sent_msg()


schedule.every(6).seconds.do(send_screenshot)

while True:
    schedule.run_pending()
    sleep(1)

from datetime import datetime, timedelta
from time import sleep

import pyautogui as gui
import schedule
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from clipboard import clipboard as clip

chrome_driver = 'D:\driver\chromedriver.exe'
chrome_options = Options()
# 设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
#  解决“chrome正受到自动测试软件的控制”信息栏显示，使用disable-infobars属性不生效问题
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
driver.get('https://www.baidu.com')

driver.maximize_window()
driver.find_element_by_id('kw').send_keys('当前时间')
driver.find_element_by_id('su').click()
sleep(5)


def sent_msg():
    # 从剪切板中获取内容
    gui.hotkey('ctrl', 'v')
    # 发送内容
    gui.hotkey('enter')


def get_text():
    date_format = "%Y-%m-%d %H:%M:%S"
    end = datetime.now()
    str_end = end.strftime(date_format)
    start = end - timedelta(seconds=30)
    str_start = start.strftime(date_format)
    result = "时间段：[%s - %s]，系统正常" % (str_start, str_end)
    return result


def send_screenshot():
    # 截取当前窗口，并指定截图图片的保存位置
    path = "D:\\baidu_img.png"
    # 刷新
    driver.refresh()
    # 全屏
    driver.maximize_window()
    sleep(5)
    driver.get_screenshot_as_file(path)
    clip.setText(get_text())
    sent_msg()
    clip.setImage(path)
    sent_msg()


schedule.every(30).seconds.do(send_screenshot)

while True:
    schedule.run_pending()
    sleep(1)

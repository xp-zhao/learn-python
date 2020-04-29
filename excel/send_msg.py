import time
from datetime import datetime, timedelta

import pyautogui as gui

from clipboard import clipboard as clip


def sent_msg():
    # 从剪切板中获取内容
    gui.hotkey('ctrl', 'v')
    # 发送内容
    gui.hotkey('enter')


def get_text():
    date_format = "%Y-%m-%d %H:%M:%S"
    end = datetime.now()
    str_end = end.strftime(date_format)
    start = end - timedelta(minutes=30)
    str_start = start.strftime(date_format)
    result = "时间段：[%s - %s]，系统正常" % (str_start, str_end)
    return result


time.sleep(10)
clip.setText("消息测试")
sent_msg()
clip.setImage("D:\\baidu_img.png")
sent_msg()

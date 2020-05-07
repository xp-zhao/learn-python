from datetime import datetime, timedelta
from io import BytesIO

import pyperclip
import win32clipboard as clip
import win32con
from PIL import Image
from time import time, sleep


# 往剪贴板中放入内容

# 将图片放入剪切板
def setImage(path):
    img = Image.open(path)  # Image.open可以打开网络图片与本地图片。
    output = BytesIO()  # BytesIO实现了在内存中读写bytes
    img.convert("RGB").save(output, "BMP")  # 以RGB模式保存图像
    data = output.getvalue()[14:]
    output.close()
    clip.OpenClipboard()  # 打开剪贴板
    clip.EmptyClipboard()  # 先清空剪贴板
    sleep(1)
    clip.SetClipboardData(win32con.CF_DIB, data)  # 将图片放入剪贴板
    clip.CloseClipboard()


# 将文字放入剪切板
def setText(data):
    pyperclip.copy(data)


if __name__ == '__main__':
    # setImage('D:\\baidu_img.png')
    # setText("文字测试")
    date_format = "%Y-%m-%d %H:%M:%S"
    end = datetime.now()
    str_end = end.strftime(date_format)
    start = end - timedelta(minutes=30)
    str_start = start.strftime(date_format)
    result = "时间段：[%s - %s]，系统正常" % (str_start, str_end)
    print(result)

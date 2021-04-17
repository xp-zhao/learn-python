import random

import time
import uiautomator2 as u2

# d = u2.connect('http：//192.168.48.200')
d = u2.connect()
print(d.info)

# 打开支付宝
print('启动支付宝')
d.app_start('com.eg.android.AlipayGphone')
time.sleep(1)
print('打开蚂蚁森林')
d(text='蚂蚁森林').click()
time.sleep(3)


def collectEnergy(count: int) -> None:
    print("开始第%d次偷能量：" % count)
    # 开始扫描点击有能力出现的区域
    for x in range(150, 1000, 150):
        for y in range(600, 900, 150):
            d.long_click(x + random.randint(10, 20), y + random.randint(10, 20), 0.1)
            time.sleep(0.01)
            if cnt != 1:
                d.click(536, 1816)


cnt = 1
while True:
    collectEnergy(cnt)
    a = d.xpath("//*[@resource-id='J_tree_dialog_wrap']").get().bounds
    d.click(1000, a[3] - 80)  # 找能量按钮的坐标
    # 如果页面出现了“返回我的森林”说明已经没有能量可偷了，结束
    if d.xpath('//*[@text="返回我的森林"]').click_exists(timeout=2.0):
        break
    cnt += 1
print("###结束###")

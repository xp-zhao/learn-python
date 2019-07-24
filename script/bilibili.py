# 拖拽验证

"""
解题思路：
1.找到验证码的图片
2.对比bg和fullbg两张图片，找到缺口位置
3.用selenium模拟人的行为拖动滑块
4.验证结果
"""
import time
from io import BytesIO
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BORDER = 6
INIT_LEFT = 60


class CrackBilibili():
    def __init__(self):
        self.url = 'https://www.v2ex.com'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        # self.email = EMAIL
        # self.password = PASSWORD

    def __del__(self):
        self.browser.close()

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return:
        """
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="geetest-wrap"]/ul/li[5]/a[1]')))
        return button

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        time.sleep(2)
        img = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="Main"]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/div[1]')))
        print(img)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()  # 获取当前页面的截图
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置1', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)

    def login(self):
        """
        登录
        :return: None
        """
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')

    def crack(self):
        # 输入用户名密码
        self.open()

        #  获取验证码图片
        # image = self.get_geetest_image('captcha.png')
        # time.sleep(2)
        # chaojiying = Chaojiying_Client('gaoyu123', '12345678', '96001')
        # im = open('captcha.png', 'rb').read()
        # result = chaojiying.PostPic(im, 3007)
        # pic_str = result['pic_str']

        # yanzhen = self.wait.until(EC.presence_of_element_located(
        #     (By.XPATH, '//*[@id="Main"]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input')))
        # yanzhen.send_keys(pic_str)

        # button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Main"]/div[2]/div[2]/form/table/tbody/tr[4]/td[2]/input[2]')))
        # button.click()
        # time.sleep(2)
        # button1 = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Rightbar"]/div[4]/div/a')))
        # button1.click()
        # time.sleep(2)
        # button2 = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Main"]/div[2]/div[2]/input')))
        # button2.click()
        time.sleep(5)


if __name__ == '__main__':
    crack = CrackBilibili()
    crack.crack()

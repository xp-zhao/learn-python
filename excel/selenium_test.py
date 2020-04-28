from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_driver = 'D:\driver\chromedriver.exe'
chrome_options = Options()
# 设置chrome浏览器无界面模式
# chrome_options.add_argument('--headless')
#  解决“chrome正受到自动测试软件的控制”信息栏显示，使用disable-infobars属性不生效问题
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
driver = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)
# driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('https://www.baidu.com')

driver.maximize_window()
driver.find_element_by_id('kw').send_keys('Java')
driver.find_element_by_id('su').click()
sleep(5)

# 截取当前窗口，并指定截图图片的保存位置
driver.get_screenshot_as_file("D:\\baidu_img.png")
# 关闭浏览器
driver.quit()

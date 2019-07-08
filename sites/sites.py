from selenium import webdriver
from utils.driverutils import DriverUtils
import time


class Naver(object):
    def __init__(self, user_id, user_pw):
        self.ID = user_id
        self.PW = user_pw

        # Web Driver 옵션 추가
        options = webdriver.ChromeOptions()
        options.add_argument("disable-gpu")
        options.add_argument('window-size=1920x1080')
        options.add_argument("lang=ko_KR")
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36')
        options.add_argument("user-data-dir=\\user-data\\naver\\")
        self.driver = webdriver.Chrome("/Users/seokjaehong/Downloads/chrome_driver/chromedriver",
                                       chrome_options=options)
        self.driver.get('https://naver.com')
        self.explicit_wait_time = 1
        self.driver_utils = DriverUtils(self.driver)

    def excute_script_login(self, user_id, user_pw):
        self.driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()
        time.sleep(2)

        self.driver.execute_script("document.getElementsByName('id')[0].value=\'" + user_id + "\'")
        self.driver.execute_script("document.getElementsByName('pw')[0].value=\'" + user_pw + "\'")
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

from bs4 import BeautifulSoup as bs4
from selenium import webdriver

from user_info import PETER_PAN_URL
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

        # self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        # self.driver.get('https://cafe.naver.com/kig')

    def move_to_new_url(self, url):
        time.sleep(2)
        self.driver.get(url)
        # self.explicit_wait_time = 1
        # self.driver_utils = DriverUtils(self.driver)

    def get_to_information(self):
        # self.driver.find_element_by_xpath(xpath).click()
        # print(self.driver)
        #
        base_url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=10322296&search.menuid=1104&search.boardtype=L'

        self.driver.get(base_url + '&search.menuid=1104&search.page=1')
        self.driver.switch_to.frame('cafe_main')
        soup = bs4(self.driver.page_source, 'html.parser')
        t = soup.select(
            '#main-area > div:nth-child(5) > table > tbody > tr:nth-child(1) > td.td_article > div.board-list > div > a')
        print(t)
        # html = self.driver.page_source
        # list_= self.driver.find_element_by_xpath('#main-area > div:nth-child(5) > table > tbody')
        # list_ = self.driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody')
        # print('html')
        # print(html)

        # soup = bs4(html, 'html.parser')
        # print('soup')
        # print(soup)
        # list = soup.select('#main-area')
        # list = soup.select()
        # print(list_)
        # for i in list_:
        #     print(i.text.strip())

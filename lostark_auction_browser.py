# -*- coding: utf-8 -*-
"""
    로스트 아크 관련 URL 정보들.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import system_info
import user_info
import lost_ark_info


class LostArckAuctionBrowser:
    driver = None
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=system_info.CHROME_DRIVER_PATH)
        # 묵시적 대기, 활성화를 위해 15 초까지 기다린다.
        self.driver.implicitly_wait(15)

        # 페이지 가져오기(이동)
        print("123123")
        self.driver.get(lost_ark_info.LOGIN_URL)
        print("aaaaaa")
        id_window = self.driver.find_element_by_css_selector('#user_id')
        print("bbbb")
        pwd_window = self.driver.find_element_by_css_selector('#user_pwd')
        print("ccccc")
        id_window.send_keys(user_info.ID)
        pwd_window.send_keys(user_info.PWD)
        pwd_window.send_keys(Keys.ENTER)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bingo-event-img")))

        # 경매장 페이지 열기
        self.driver.get(lost_ark_info.AUCTION_URL)


    def __del__(self):
        print("destroy")
        self.driver.quit()


    





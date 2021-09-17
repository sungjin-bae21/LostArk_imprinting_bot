# -*- coding: utf-8 -*-
"""
    로스트 아크 관련 URL 정보들.
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import system_info
import user_info
import lost_ark_info

## TODO : 아이템 종류가 다를때 특성, 각인 선택 부분이 달라지는데 동작하기 때문에 지금은 넘어간다.
class LostArckAuctionBrowser:
    driver = None
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=system_info.CHROME_DRIVER_PATH)
        # 묵시적 대기, 활성화를 위해 15 초까지 기다린다.
        self.driver.implicitly_wait(15)

        # 페이지 가져오기(이동)
        self.driver.get(lost_ark_info.LOGIN_URL)
        id_window = self.driver.find_element_by_css_selector('#user_id')
        pwd_window = self.driver.find_element_by_css_selector('#user_pwd')
        id_window.send_keys(user_info.ID)
        pwd_window.send_keys(user_info.PWD)
        pwd_window.send_keys(Keys.ENTER)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bingo-event-img")))

        # 경매장 페이지 열기
        self.driver.get(lost_ark_info.AUCTION_URL)

    # 상세 검색으로 데이터 찾기.
    # 입력 정보 장신구 종류, 각인 + 5, 각인 + 3, 최소 품질
    # 평균 가중치의 정보를 넘겨준다.
    def SearchItem(self, item_type, bonus_index, bonus_index2, quality, stats, stats2 = -1):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lostark-wrapper > div > main > div > div.deal > div.deal-contents > form > fieldset > div > div.bt > button.button.button--deal-detail")))
        
        detail_search_window = self.driver.find_element_by_css_selector('#lostark-wrapper > div > main > div > div.deal > div.deal-contents > form > fieldset > div > div.bt > button.button.button--deal-detail')
        detail_search_window.click()

        # 아이템 타입 설정.
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selCategoryDetail")))
        item_category_window = self.driver.find_element_by_css_selector("#selCategoryDetail")
        item_category_window.click()

        if item_type == 1:  # 목걸이
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selCategoryDetail > div.lui-select__option > label:nth-child(11)")))
            temp_button = self.driver.find_element_by_css_selector('#selCategoryDetail > div.lui-select__option > label:nth-child(11)')
            temp_button.click()
        elif item_type == 2: # 반지
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selCategoryDetail > div.lui-select__option > label:nth-child(13)")))
            temp_button = self.driver.find_element_by_css_selector('#selCategoryDetail > div.lui-select__option > label:nth-child(13)')
            temp_button.click()
        elif item_type == 3: # 귀걸이
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selCategoryDetail > div.lui-select__option > label:nth-child(12)")))
            temp_button = self.driver.find_element_by_css_selector('#selCategoryDetail > div.lui-select__option > label:nth-child(12)')
            temp_button.click()
        else : # 돌
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selCategoryDetail > div.lui-select__option > label:nth-child(9)")))
            temp_button = self.driver.find_element_by_css_selector('#selCategoryDetail > div.lui-select__option > label:nth-child(9)')
            temp_button.click()

        # 아이템 등급 설정 팝업
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div")))
        item_grade_window = self.driver.find_element_by_css_selector("#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div")
        item_grade_window.click()

        # 유물로 선택
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > div.lui-select__option > label:nth-child(7)")))
        temp_button = self.driver.find_element_by_css_selector("#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > div.lui-select__option > label:nth-child(7)")
        temp_button.click()

        # 티어 선택
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div.lui-select__title")))
        temp_button = self.driver.find_element_by_css_selector("#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div.lui-select__title")
        temp_button.click()

        # 3 티어로 선택
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div.lui-select__option > label:nth-child(4)")))
        temp_button = self.driver.find_element_by_css_selector("#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div.lui-select__option > label:nth-child(4)")
        temp_button.click()

        # 돌이 아닌 경우 품질 선택필요
        # 베타 버전이기 떄문에 품질 70 이상을 확인하는 식으로 한다
        if item_type != 3:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(4) > div > div.lui-select__title")))
            temp_button = self.driver.find_element_by_css_selector("#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(4) > div > div.lui-select__title")
            temp_button.click()

            # 품질 70 이상으로 선택
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(4) > div > div.lui-select__option > label:nth-child(8)")))
            temp_button = self.driver.find_element_by_css_selector("#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(4) > div > div.lui-select__option > label:nth-child(8)")
            temp_button.click()
            print("yes")

        # 기타 상세옵션 1 활성화
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtc_0")))
        temp_button = self.driver.find_element_by_css_selector("#selEtc_0")
        temp_button.click()

        # 기타 상세옵션 1 각인으로 설정
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#selEtc_0 > div.lui-select__option > label:nth-child(3)')))
        temp_button = self.driver.find_element_by_css_selector('#selEtc_0 > div.lui-select__option > label:nth-child(3)')
        temp_button.click()

        # 기타 상세옵션 2 활성화
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtc_1")))
        temp_button = self.driver.find_element_by_css_selector("#selEtc_1")
        temp_button.click()

        # 기타 상세옵션 2 각인으로 설정
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtc_1 > div.lui-select__option > label:nth-child(3)")))
        temp_button = self.driver.find_element_by_css_selector("#selEtc_1 > div.lui-select__option > label:nth-child(3)")
        temp_button.click()
        
        # +5 각인 설정 활성화.
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_0")))
        temp_button = self.driver.find_element_by_css_selector("#selEtcSub_0")
        temp_button.click()

        # +5 각인 옵션 설정
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_0 > div.lui-select__option > label:nth-child({index})".format(index=bonus_index))))
        temp_button = self.driver.find_element_by_css_selector("#selEtcSub_0 > div.lui-select__option > label:nth-child({index})".format(index=bonus_index))
        temp_button.click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#txtEtcMin_0")))
        temp_button = self.driver.find_element_by_css_selector("#txtEtcMin_0")
        temp_button.send_keys(5)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#txtEtcMax_0")))
        temp_button = self.driver.find_element_by_css_selector("#txtEtcMax_0")
        temp_button.send_keys(5)

        # +3 각인 설정 활성화
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_1")))
        temp_button = self.driver.find_element_by_css_selector("#selEtcSub_1")
        temp_button.click()

        # +3 각인 옵션 설정
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_1 > div.lui-select__option > label:nth-child({index})".format(index=bonus_index2))))
        temp_button = self.driver.find_element_by_css_selector("#selEtcSub_1 > div.lui-select__option > label:nth-child({index})".format(index=bonus_index2))
        temp_button.click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#txtEtcMin_1")))
        temp_button = self.driver.find_element_by_css_selector("#txtEtcMin_1")
        temp_button.send_keys(3)

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#txtEtcMax_1")))
        temp_button = self.driver.find_element_by_css_selector("#txtEtcMax_1")
        temp_button.send_keys(3)
        
        if item_type != 4:
            
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtc_2")))
            temp_button = self.driver.find_element_by_css_selector("#selEtc_2")
            temp_button.click()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtc_2 > div.lui-select__option > label:nth-child(2)")))
            temp_button = self.driver.find_element_by_css_selector("#selEtc_2 > div.lui-select__option > label:nth-child(2)")
            temp_button.click()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_2")))
            temp_button = self.driver.find_element_by_css_selector("#selEtcSub_2")
            temp_button.click()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_2 > div.lui-select__option > label:nth-child({index})".format(index=stats))))
            temp_button = self.driver.find_element_by_css_selector("#selEtcSub_2 > div.lui-select__option > label:nth-child({index})".format(index=stats))
            temp_button.click()

            if stats2 != -1:
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtc_3")))
                temp_button = self.driver.find_element_by_css_selector("#selEtc_3")
                temp_button.click()

                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtc_3 > div.lui-select__option > label:nth-child(2)")))
                temp_button = self.driver.find_element_by_css_selector("#selEtc_3 > div.lui-select__option > label:nth-child(2)")
                temp_button.click()

                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_3")))
                temp_button = self.driver.find_element_by_css_selector("#selEtcSub_3")
                temp_button.click()

                
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#selEtcSub_3 > div.lui-select__option > label:nth-child({index})".format(index=stats2))))
                temp_button = self.driver.find_element_by_css_selector("#selEtcSub_3 > div.lui-select__option > label:nth-child({index})".format(index=stats2))
                temp_button.click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-deal-option > div > div > div.lui-modal__button > button.lui-modal__search")))
        temp_button = self.driver.find_element_by_css_selector("#modal-deal-option > div > div > div.lui-modal__button > button.lui-modal__search")
        temp_button.click()

        # 이미지
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#auctionListTbody > tr:nth-child(1) > td:nth-child(1) > div.grade > span.slot > img")))
        # 품질
        temp_button = self.driver.find_element_by_css_selector("#auctionListTbody > tr:nth-child(1) > td:nth-child(3) > div > span.txt")
        target_quality = int(temp_button.text)
        # 가격
        temp_button = self.driver.find_element_by_css_selector("#auctionListTbody > tr:nth-child(1) > td:nth-child(6) > div > em")
        money_str = temp_button.text.replace(",","")
        print(money_str)
        target_price = int(money_str)

        return target_price / target_quality
        
       

        

    def __del__(self):
        print("destroy")
        self.driver.quit()


    





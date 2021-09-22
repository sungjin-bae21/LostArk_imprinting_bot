# -*- coding: utf-8 -*-
"""
    로스트 아크 관련 URL 정보들.
"""
import time
from warnings import catch_warnings

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select

import system_info
import user_info
import lost_ark_info


def wait_for_element_located(driver, by, name_str):
    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, name_str)))
    return element


def wait_for_not_element_located(driver, by, name_str):
    WebDriverWait(driver, 5).until_not(EC.presence_of_element_located((by, name_str)))


def element_click(driver, by, name_str):
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((by, name_str))).click()

def wait_for_page_load(driver, timeout=30):
    old_page = driver.find_element_by_tag_name('html')
    yield
    WebDriverWait(driver, timeout).until(
        driver.staleness_of(old_page)
    )



## TODO : 아이템 종류가 다를때 특성, 각인 선택 부분이 달라지는데 동작하기 때문에 지금은 넘어간다.
class LostArckAuctionBrowser:
    driver = None
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(executable_path=system_info.CHROME_DRIVER_PATH, options=options)
        # 묵시적 대기, 활성화를 위해 15 초까지 기다린다.
        self.driver.implicitly_wait(15)

        # 페이지 가져오기(이동)
        self.driver.get(lost_ark_info.LOGIN_URL)
        id_window = wait_for_element_located(self.driver, By.CSS_SELECTOR, "#user_id")
        pwd_window = wait_for_element_located(self.driver, By.CSS_SELECTOR, "#user_pwd")
        id_window.send_keys(user_info.ID)
        pwd_window.send_keys(user_info.PWD)
        pwd_window.send_keys(Keys.ENTER)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bingo-event-img")))

        # 경매장 페이지 열기
        self.driver.get(lost_ark_info.AUCTION_URL)
        self.driver.implicitly_wait(15)
        wait_for_page_load(self.driver)

        
    def init_select_option_datas(self):
        # 상세 검색
        element_click(self.driver, By.CSS_SELECTOR,
                      "#lostark-wrapper > div > main > div > div.deal > div.deal-contents > form > fieldset > div > div.bt > button.button.button--deal-detail")
        
        # 직업 전체로 변경
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selClassDetail > div.lui-select__title")

        element_click(self.driver, By.CSS_SELECTOR,
                      " #selClassDetail > div.lui-select__option > label:nth-child(1)")

        option_list_count = len(
            self.driver.find_elements_by_css_selector(
                "#selEtc_0 > div.lui-select__option label"))

        # 상세 옵션의 index 가 올바른지 확인 및 수정.
        i = 1
        while i < option_list_count:
            i += 1
            text_data = wait_for_element_located(self.driver, By.CSS_SELECTOR,
                "#selEtc_0 > div.lui-select__option > label:nth-child({index})".format(index=i)).get_attribute("innerText") 
            lost_ark_info.OPTION_SELECT_TABLE.append((text_data,i))

        # 상세 리스트 클릭
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_0 > div.lui-select__title")

        # 각인 옵션 클릭.
        option_idx = lost_ark_info.option_name_to_index("각인 효과")
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_0 > div.lui-select__option > label:nth-child({index})".format(index=option_idx))

        # 각인 목록의 길이 확인
        option_list_count = len(
            self.driver.find_elements_by_css_selector(
                "#selEtcSub_0 > div.lui-select__option label"))

        i = 1
        while i < option_list_count:
            i += 1
            text_data = wait_for_element_located(self.driver, By.CSS_SELECTOR,
                "#selEtcSub_0 > div.lui-select__option > label:nth-child({index})".format(index=i)).get_attribute("innerText")
            lost_ark_info.BONUS_TABLE.append((text_data, i))

        # 상세 리스트 클릭
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_1 > div.lui-select__title")

        # 각인 옵션 클릭.
        option_idx = lost_ark_info.option_name_to_index("전투 특성")
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_1 > div.lui-select__option > label:nth-child({index})".format(index=option_idx))

        # 각인 목록의 길이 확인
        option_list_count = len(
            self.driver.find_elements_by_css_selector(
                "#selEtcSub_1 > div.lui-select__option label"))


        # 상세 옵션의 index 가 올바른지 확인 및 수정.
        i = 1
        while i < option_list_count:
            i += 1
            text_data = wait_for_element_located(self.driver, By.CSS_SELECTOR,
                "#selEtcSub_1 > div.lui-select__option > label:nth-child({index})".format(index=i)).get_attribute("innerText")
            lost_ark_info.STATS_TABLE.append((text_data, i))


    # 상세 검색으로 데이터 찾기.
    # 입력 정보 장신구 종류, 각인 + 5, 각인 + 3, 최소 품질
    # 평균 가중치의 정보를 넘겨준다.
    def SearchItem(self, item_type, bonus_index, bonus_index2, quality, stats, stats2 = -1):
        element_click(self.driver, By.CSS_SELECTOR,
                      "#lostark-wrapper > div > main > div > div.deal > div.deal-contents > form > fieldset > div > div.bt > button.button.button--deal-detail")

        # 직업 전체로 변경
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selClassDetail > div.lui-select__title")

        element_click(self.driver, By.CSS_SELECTOR,
                      " #selClassDetail > div.lui-select__option > label:nth-child(1)")

        # 아이템 타입 설정.
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selCategoryDetail")

        element_click(self.driver, By.CSS_SELECTOR,
                      "#selCategoryDetail > div.lui-select__option > label:nth-child({index})".format(index=item_type))

        # 아이템 등급 설정 팝업
        element_click(self.driver, By.CSS_SELECTOR,
                      "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div")
       
        # 유물로 선택
        element_click(self.driver, By.CSS_SELECTOR,
                      "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2) > div > div.lui-select__option > label:nth-child(7)")

        # 티어 선택
        element_click(self.driver, By.CSS_SELECTOR,
                      "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div.lui-select__title")

        # 3 티어로 선택
        element_click(self.driver, By.CSS_SELECTOR,
                      "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > div > div.lui-select__option > label:nth-child(4)")

        # 돌이 아닌 경우 품질 선택필요
        # 베타 버전이기 떄문에 품질 70 이상을 확인하는 식으로 한다
        if item_type != 9:
            element_click(self.driver, By.CSS_SELECTOR,
                          "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(4) > div > div.lui-select__title")
           
            # 품질 70 이상으로 선택
            element_click(self.driver, By.CSS_SELECTOR,
                          "#modal-deal-option > div > div > div.lui-modal__content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(4) > div > div.lui-select__option > label:nth-child(8)")

        print("aaaa")
        # 기타 상세옵션 1 활성화
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_0")

        print("bbbbb")

        # 기타 상세옵션 1 각인으로 설정
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_0 > div.lui-select__option > label:nth-child(3)")

        print("ccccc")
        # 기타 상세옵션 2 활성화
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_1")

        # 기타 상세옵션 2 각인으로 설정
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtc_1 > div.lui-select__option > label:nth-child(3)")

        # +5 각인 설정 활성화.
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtcSub_0")

        # +5 각인 옵션 설정
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtcSub_0 > div.lui-select__option > label:nth-child({index})".format(index=bonus_index))

        # 최소값 설정
        element = wait_for_element_located(self.driver, By.CSS_SELECTOR, "#txtEtcMin_0")
        element.send_keys(5)
     
        # 최대값 설정
        element = wait_for_element_located(self.driver, By.CSS_SELECTOR, "#txtEtcMax_0")
        element.send_keys(5)
        

        # +3 각인 설정 활성화
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtcSub_1")

        # +3 각인 옵션 설정
        element_click(self.driver, By.CSS_SELECTOR,
                      "#selEtcSub_1 > div.lui-select__option > label:nth-child({index})".format(index=bonus_index2))

        # 최소값 설정
        element = wait_for_element_located(self.driver, By.CSS_SELECTOR, "#txtEtcMin_1")
        element.send_keys(3)
        
        # 최대값 설정
        element = wait_for_element_located(self.driver, By.CSS_SELECTOR, "#txtEtcMax_1")
        element.send_keys(3)
       
        # 첫번째 전투특성
        if item_type != 9:
            element_click(self.driver, By.CSS_SELECTOR,
                          "#selEtc_2")
            
            element_click(self.driver, By.CSS_SELECTOR,
                          "#selEtc_2 > div.lui-select__option > label:nth-child(2)")

            element_click(self.driver, By.CSS_SELECTOR,
                          "#selEtcSub_2")

            element_click(self.driver, By.CSS_SELECTOR,
                          "#selEtcSub_2 > div.lui-select__option > label:nth-child({index})".format(index=stats))

            # 두번째 전투특성
            if stats2 != -1:
                element_click(self.driver, By.CSS_SELECTOR,
                              "#selEtc_3")

                element_click(self.driver, By.CSS_SELECTOR,
                              "#selEtc_3 > div.lui-select__option > label:nth-child(2)")

                element_click(self.driver, By.CSS_SELECTOR,
                              "#selEtcSub_3")

                element_click(self.driver, By.CSS_SELECTOR,
                              "#selEtcSub_3 > div.lui-select__option > label:nth-child({index})".format(index=stats2))

        # 검색
        element_click(self.driver, By.CSS_SELECTOR,
                      "#modal-deal-option > div > div > div.lui-modal__button > button.lui-modal__search")

        # 검색 결과가 없는지 확인필요.
        try:
            wait_for_not_element_located(self.driver, By.CLASS_NAME, "empty")
        except TimeoutException:
            print("item is not empty")
        finally:
            print("item is empty")

        # 가격순으로 정렬
        element_click(self.driver, By.CSS_SELECTOR,
                      "#BUY_PRICE")
        
        # 이미지 클릭이 가능한지 확인해 로딩이 완료되었는지 확인한다.
        element_click(self.driver, By.CSS_SELECTOR,
                      "#auctionListTbody > tr:nth-child(1) > td:nth-child(1) > div.grade > span.slot > img")
        
        # 품질
        temp_quailty = wait_for_element_located(self.driver, By.CSS_SELECTOR,
                                                "#auctionListTbody > tr:nth-child(1) > td:nth-child(3) > div > span.txt")
        print("품질 : {aaa}".format(aaa=temp_quailty))
        target_quality = int(temp_quailty.text)

        # 가격
        temp_quailty = wait_for_element_located(self.driver, By.CSS_SELECTOR,
                                                "#auctionListTbody > tr:nth-child(1) > td:nth-child(6) > div > em")
        print("가격 : /{aaa}/".format(aaa=temp_quailty))
     
        temp_button = self.driver.find_element_by_css_selector("#auctionListTbody > tr:nth-child(1) > td:nth-child(6) > div > em")
        money_str = temp_button.text.replace(",","")
        target_price = int(money_str)

        return target_price / target_quality

        
    def __del__(self):
        print("destroy")
        self.driver.quit()


    





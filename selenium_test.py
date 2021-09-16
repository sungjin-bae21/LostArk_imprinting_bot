# -*- coding: utf-8 -*-

"""
   메인 로직을 표현.
"""


# selenium의 webdriver를 가져온다.
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import lost_ark_info
import user_info
import system_info

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument(argument='--headless')
# chrome_option.add_argument(argument='--no-sandbox')
# chrome_option.add_argument(argument='disable-dev-shm-usage')

# brew 로 설치된 chromedriver의 path
# driver_path = "/Library/Frameworks/Python.framework/Versions/3.9/chromedriver-Darwin"

# 크롬 드라이버를 사용
chrome_driver = webdriver.Chrome(executable_path=system_info.CHROME_DRIVER_PATH)
# chrome_driver = webdriver.Chrome(executable_path=driver_path, options=chrome_option)
# 묵시적 대기, 활성화를 위해 15 초까지 기다린다.
chrome_driver.implicitly_wait(15)

# 페이지 가져오기(이동)
chrome_driver.get(lost_ark_info.LOGIN_URL)
id_input_window = chrome_driver.find_element_by_css_selector('#user_id')
pwd_input_window = chrome_driver.find_element_by_css_selector('#user_pwd')
id_input_window.send_keys(user_info.ID)
pwd_input_window.send_keys(user_info.PWD)
pwd_input_window.send_keys(Keys.ENTER)

wait = WebDriverWait(chrome_driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bingo-event-img")))
chrome_driver.get(lost_ark_info.ACTION_URL)

time.sleep(2)
chrome_driver.quit()

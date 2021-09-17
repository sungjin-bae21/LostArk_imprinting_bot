# -*- coding: utf-8 -*-
"""
    어떻게 각인을 마출지 계산해주는 클래스.
"""

import time
import lost_ark_info
from lostark_auction_browser import LostArckAuctionBrowser

class PurchasingRepresentative():
    def work(self, character_data):
        action = LostArckAuctionBrowser()

        # 목걸이 검색.
        # 5 개의 가능한 조합중 가장 싼 것을 선택한다.
        price = action.SearchItem(1,25,37,1, 2, 5)
        print(price)
        time.sleep(100)
        # 돌 검색

        # 목걸이 검색

        # 귀걸이 검색

    
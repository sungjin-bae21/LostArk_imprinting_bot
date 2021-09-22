# -*- coding: utf-8 -*-
"""
    어떻게 각인을 마출지 계산해주는 클래스.
"""

import time
import lost_ark_info
import sys
from lostark_auction_browser import LostArckAuctionBrowser
from selenium.common.exceptions import TimeoutException

class PurchasingRepresentative():
    def work(self, character_data):
        action = LostArckAuctionBrowser()

        n = len(character_data.bonus_idxs)
        i = 0
        j = 0
        pivot = [-1, -1]
        min = sys.float_info.max
        while i < n - 1:
            j = i + 1
            while j < n:
                msg1 = lost_ark_info.bonus_index_to_string(character_data.bonus_idxs[i])
                msg2 = lost_ark_info.bonus_index_to_string(character_data.bonus_idxs[j])
                print(msg1)
                print(msg2)
                try:
                    max = action.SearchItem(11, character_data.bonus_idxs[i], character_data.bonus_idxs[j], 0, character_data.stats_idxs[0], character_data.stats_idxs[1])
                    if max < min:
                        pivot[0] = character_data.bonus_idxs[i]
                        pivot[1] = character_data.bonus_idxs[j]
                except TimeoutException:
                    print("new browser make")
                    action = LostArckAuctionBrowser()
                    j = j -1
                j = j + 1
            i = i + 1

        msg1 = lost_ark_info.bonus_index_to_string(pivot[0])
        msg2 = lost_ark_info.bonus_index_to_string(pivot[1])
        return "저렴한 목걸이의 각인은 +5 {first} +3 {second} 입니다".format(first=msg1, second=msg2)

        # 돌 검색

        # 목걸이 검색

        # 귀걸이 검색

    
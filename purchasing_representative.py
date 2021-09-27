# -*- coding: utf-8 -*-
"""
    어떻게 각인을 마출지 계산해주는 클래스.
"""

import time
import lost_ark_info
import sys
from lostark_auction_browser import LostArckAuctionBrowser
from selenium.common.exceptions import TimeoutException


# 가격 / 퀠리티
def get_price_out_of_quality(items):
    n = len(items)
    total_price = 0
    total_quality = 0
    i = 0
    while i < n:
        if items[i].price == -1 or items[i].quality == -1:
            print("items info is not initialized")

        total_price = items[i].price
        total_quality = items[i].quality
        i += 1
    return total_price / total_quality


class PurchasingRepresentative():
    def init_data(self):
        action = LostArckAuctionBrowser()
        action.init_select_option_datas()


    # 목걸이 리스트를 보관하는 식으로 하자.
    def find_checp_necklace(self, action, character_data):
        # 이중 포문으로 목걸이 리스트를 긁어 온다.
        n = len(character_data.bonus_idxs)

        i = 0
        j = 0
        price_out_fot_quality = sys.float_info.max
        checp_item = lost_ark_info.ItemInfo()
        while i < n - 1:
            j = i + 1
            while j < n:
                items = action.SearchItem(
                            11,                           # 목걸이 타입
                            #lost_ark_info.bonus_name_to_index("원한"),
                            #lost_ark_info.bonus_name_to_index("슈퍼 차지"),
                            character_data.bonus_idxs[i], # +5 각인
                            character_data.bonus_idxs[j], # +3 각인
                            0,                            # 퀄리티 현재 적용안됨.
                            character_data.stats_idxs[0], # 스탯 1
                            character_data.stats_idxs[1]) # 스탯 2

                if len(items) > 0:
                    new_price_out_fot_quality = get_price_out_of_quality(items)
                    if new_price_out_fot_quality < price_out_fot_quality:
                        checp_item = items[0]
                j = j + 1
            i = i + 1
        return checp_item


    def work(self, character_data):
        action = LostArckAuctionBrowser()
        necklaces = self.find_checp_necklace(action, character_data)
        print(necklaces)

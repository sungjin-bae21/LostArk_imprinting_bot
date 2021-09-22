# -*- coding: utf-8 -*-
"""
    로스트 아크 관련 정보들.
"""

MAIN_URL = "https://lostark.game.onstove.com/Main"
AUCTION_URL = "https://lostark.game.onstove.com/Auction"
LOGIN_URL = "https://member.onstove.com/auth/login"

# 리스ㄹ트 로수정
BONUS_TABLE = []


STATS_TABLE = []


ITEM_TYPE_TABLE = [("목걸이", 11),
                   ("반지", 13),
                   ("귀걸이", 12),
                   ("어빌리티 스톤", 9)]


OPTION_SELECT_TABLE = []

def option_name_to_index(option_name):
    for data in OPTION_SELECT_TABLE:
        if data[0] == option_name:
            return data[1]

    print("Error : " + option_name + " isn't in the table")
    return -1


def bonus_name_to_index(bonus_name):
    for data in BONUS_TABLE:
        if data[0] == bonus_name:
            return data[1]

    print("Error : " + bonus_name + " isn't in the table")
    return -1


def bonus_index_to_string(index):
    for data in BONUS_TABLE:
        if data[1] == index:
            return data[0]

    print("Error : bonus " + index + " isn't in the table")
    return -1


def stats_name_to_index(stats_name):
    for data in STATS_TABLE:
        if data[0] == stats_name:
            return data[1]

    print("Error : " + stats_name + " isn't in the table")
    return -1


def stats_index_to_string(index):
    for data in STATS_TABLE:
        if data[1] == index:
            return data[0]

    print("Error : stats " + index + " isn't in the table")
    return -1


def item_type_to_index(item_type):
    for data in ITEM_TYPE_TABLE:
        if data[0] == item_type:
            return data[1]

    print("Error : " + item_type + " isn't in the table")
    return -1


def item_index_to_type(index):
    for data in ITEM_TYPE_TABLE:
        if data[1] == index:
            return data[0]

    print("Error : stats " + index + " isn't in the table")
    return -1


class LostArkCharacterInfo():
    bonus_idxs = []
    stats_idxs = []
    legend_book_idx = -1
    hero_book_idx = -1

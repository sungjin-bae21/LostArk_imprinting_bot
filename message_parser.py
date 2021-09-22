# -*- coding: utf-8 -*-
"""
    문자열 메세지를 데이터로 변경해준다.
"""

# 메세지는 다음과 같은 형태로 들어온다
#
# ::전설(원한) 영웅(분노의 망치), (원한)(분노의 망치)(예리한 둔기)(각성)(기습의 대가), (치명)(신속)
#
import lost_ark_info


def message_to_character_data(message):
    # 전설 각인.
    start_idx = message.find("(", 0, len(message))
    end_idx = message.find(")",start_idx, len(message))
    legend_book = message[start_idx+1 : end_idx]

    # 전설 각인.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    hero_book = message[start_idx+1 : end_idx]

    #첫번째 각인.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    first_bonus = message[start_idx+1 : end_idx]

    #두번째 각인.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    second_bonus = message[start_idx+1 : end_idx]

    #세번째 각인.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    third_bonus = message[start_idx+1 : end_idx]

    #네번째 각인.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    fourth_bonus = message[start_idx+1 : end_idx]

    #다섯번째 각인.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    fifth_bonus = message[start_idx+1 : end_idx]

    #특성 1.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    first_stats = message[start_idx+1 : end_idx]

    #특성 2.
    start_idx = message.find("(", end_idx, len(message))
    end_idx = message.find(")", start_idx, len(message))
    second_stats = message[start_idx+1 : end_idx]

    character_data = lost_ark_info.LostArkCharacterInfo()
    character_data.legend_book_idx = lost_ark_info.bonus_name_to_index(legend_book)
    character_data.hero_book_idx = lost_ark_info.bonus_name_to_index(hero_book)

    character_data.bonus_idxs.append(lost_ark_info.bonus_name_to_index(first_bonus))
    character_data.bonus_idxs.append(lost_ark_info.bonus_name_to_index(second_bonus))
    character_data.bonus_idxs.append(lost_ark_info.bonus_name_to_index(third_bonus))
    character_data.bonus_idxs.append(lost_ark_info.bonus_name_to_index(fourth_bonus))
    character_data.bonus_idxs.append(lost_ark_info.bonus_name_to_index(fifth_bonus))

    character_data.stats_idxs.append(lost_ark_info.stats_name_to_index(first_stats))
    character_data.stats_idxs.append(lost_ark_info.stats_name_to_index(second_stats))

    # TODO : 로직 수정필요 알아보기힘들다.
    # 각인서 기준으로 정렬
    pivot = 0
    for idx in character_data.bonus_idxs:
        if idx == character_data.hero_book_idx:
            pivot = idx

    if pivot != 0:
        character_data.bonus_idxs.remove(pivot)
        character_data.bonus_idxs.insert(0, pivot)

    pivot = 0
    for idx in character_data.bonus_idxs:
        if idx == character_data.legend_book_idx:
            pivot = idx

    if pivot != 0:
        character_data.bonus_idxs.remove(pivot)
        character_data.bonus_idxs.insert(0, pivot)

    return character_data

# -*- coding: utf-8 -*-
"""
    로스트 아크 관련 정보들.
"""

MAIN_URL = "https://lostark.game.onstove.com/Main"
AUCTION_URL = "https://lostark.game.onstove.com/Auction"
LOGIN_URL = "https://member.onstove.com/auth/login"


BONUS_TABLE = [("각성", 2),
               ("결투의 대가", 7),
               ("구슬 동자", 11),
               ("급소 타격", 14),
               ("기습의 대가", 15),
               ("마나의 흐름", 23),
               ("돌격 대장", 20),
               ("마나 효율 증가", 22),
               ("바리케이트", 25),
               ("번개의 분노", 27),
               ("속전속결", 36),
               ("슈퍼차지", 37),
               ("시선 집중", 39),
               ("아드레날린", 42),
               ("예리한 둔기", 50),
               ("원한", 54),
               ("저주받은 인형", 58),
               ("정기 흡수", 65),
               ("정밀 단도", 66),
               ("중갑 착용", 68),
               ("질량 증가", 72),
               ("최대 마나 증가", 74),
               ("타격의 대가", 77),
               ("폭발물 전문가", 77),
               ("광전사의 비기", 10),
               ("광기", 8),
               ("전문의", 59),
               ("전투 태세", 60),
               ("고독한 기사", 8),
               ("분노의 망치", 29),
               ("중력 수련", 69),
               ("심판자", 41),
               ("축복의 오라", 76),
               ("진실된 용맹", 70),
               ("절정", 62),
               ("절제", 63),
               ("절실한 구원", 61),
               ("상급 소환사", 33),
               ("넘치는 교감", 17),
               ("황후의 은총", 86),
               ("황제의 칙령", 85),
               ("오의강화", 51),
               ("초심", 73),
               ("충격 단련", 77),
               ("극의: 체술", 13),
               ("세맥타통", 35),
               ("역천지체", 48),
               ("죽음의 습격", 67),
               ("두 번째 동료", 21),
               ("강화 무기", 5),
               ("핸드거너", 82),
               ("연속포격", 49),
               ("화력 강화", 83),
               ("버스트", 26),
               ("잔재된 기운", 57),
               ("완벽한 억제", 53),
               ("멈출 수 없는 충동", 24),
               ("아르데타인의 기술", 43),
               ("진화의 유산", 71),
               ("갈증", 3),
               ("달의 소리", 18),
               ("사냥의 시간", 32),
               ("피스메이커", 81),
               ("일격필살", 56),
               ("오의난무", 52),
               ("점화", 64),
               ("환류", 84)]


STATS_TABLE = [("치명", 2),
               ("신속", 5),
               ("특화", 3)]


ITEM_TYPE_TABLE = [("목걸이", 1),
                   ("반지", 2),
                   ("귀걸이", 3),
                   ("어빌리티 스톤", 4)]


def bonus_name_to_index(bonus_name):
    for data in BONUS_TABLE:
        if data[0] == bonus_name:
            return data[1]

    print("Error : " + bonus_name + " isn't in the table")


def bonus_index_to_string(index):
    for data in BONUS_TABLE:
        if data[1] == index:
            return data[0]
    
    print("Error : bonus " + index + " isn't in the table")


def stats_name_to_index(stats_name):
    for data in STATS_TABLE:
        if data[0] == stats_name:
            return data[1]

    print("Error : " + stats_name + " isn't in the table")


def stats_index_to_string(index):
    for data in STATS_TABLE:
        if data[1] == index:
            return data[0]
    
    print("Error : stats " + index + " isn't in the table")


def item_type_to_index(item_type):
    for data in ITEM_TYPE_TABLE:
        if data[0] == item_type:
            return data[1]

    print("Error : " + item_type + " isn't in the table")


def item_index_to_type(index):
    for data in ITEM_TYPE_TABLE:
        if data[1] == index:
            return data[0]
    
    print("Error : stats " + index + " isn't in the table")



class LostArkCharacterInfo():
    bonus_idxs = []
    stats_idxs = []
    legend_book_idx = -1
    hero_book_idx = -1


# 참고 사이트
# https://lostarkcodex.com/us/engravings/battle/
# https://namu.wiki/w/로스트아크/각인

"""
class BonusData():
    awakening                = "각성"
    master_brawler           = "결투의 대가"
    drops_of_ether           = "구슬 동자"
    vital_point_strike       = "급소 타격"
    ambuse_master            = "기습의 대가"
    mp_regen                 = "마나의 흐름"
    raid_captain             = "돌격 대장"
    mana_efficiency_increase = "마나 효율 증가"  
    barricade                = "바리케이트"
    lightning_fury           = "번개의 분노"
    fast_casting             = "속전속결"
    super_charge             = "슈퍼차지"
    attention                = "시선 집중"
    adrenaline               = "아드레날린"
    keen_blunt_weapon        = "예리한 둔기"
    grudge                   = "원한"
    cursed_doll              = "저주받은 인형"
    spirit_absorption        = "정기 흡수"
    precision_dagger         = "정밀 단도"
    shield_piercing          = "중갑 착용"
    mass_increase            = "질량 증가"
    increased_max_mp         = "최대 마나 증가"
    driving_force            = "추진력"
    master_of_blows          = "타격의 대가"
    explosive_expert         = "폭발물 전문가"
    berserker_technique      = "광전사의 비기"
    mayhem                   = "광기"
    combat_readiness         = "전투 준비"
    solo_knight              = "고독한 기사"
    rage_hammer              = "분노의 망치"
    gravity_training         = "중력 수련"
    judgment                 = "심판자"
    blessed_aura             = "축복의 오라"
    true_courage             = "진실된 용맹"
    desperate_salvation      = "절실한 구원"
    master_summoner          = "상급 소환사"
    communication_overflow   = "넘치는 교감"
    grace_of_the_empress     = "황후의 은총"
    order_of_the_emperor     = "황제의 칙령"
    esoteric_skill_enhance   = "오의강화"
    first_intention          = "초심"
    shock_training           = "충격 단련"
    ultimate_taijutsu        = "극의: 체술"
    energy_overflow          = "세맥타통"
    robust_spirit            = "역천지제체"
    death_strike             = "죽음의 습격"
    second_companion         = "두 번째 동료"
    enhanced_weapon          = "강화 무기"
    pistoleer                = "핸드거너"
    barrage                  = "연속포격"
    firepower_enhancement    = "화력 강화"
    burst                    = "버스트"
    remaining_energy         = "잔재된 기운"
    perfect_suppression      = "완벽한 억제"
    unstoppable_drive        = "멈출 수 없는 충동"
    artetine_skills          = "아르데타인의 기술"
    legacy_of_evolution      = "진화의 유산"
    thirst                   = "갈증"
    sound_of_the_moon        = "달의 소리"
    hunting_time             = "사냥의 시간"
    peacemaker               = "피스메이커"
    one_blow_kill            = "일격필살"
    mischief                 = "오의난무"
    ignition                 = "점화"
    reflux                   = "환류"
"""



    




    

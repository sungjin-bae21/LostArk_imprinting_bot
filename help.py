# -*- coding: utf-8 -*-
"""
    사용법에 관련된 메세지
"""


def Commands():
    return "&&사용법"


def HowToUse():
    return """
           다음과 같이 사용합니다\n
           ----------각인서----------||---------필요 각인------------------------//-- 특성--\n
           ::전설(원한) 영웅(분노의 망치), (원한)(분노의 망치)(예리한 둔기)(각성)(기습의 대가), (치명)(신속)\n
           바로 위의 메세지를 복붙하고 () 안의 각인을 원하는 각인으로 변경해 입력해주세요
           """


def OnHelpMessage(message):
    if message.find("명령어") == 2:
        return Commands()

    if message.find("사용법") == 2:
        return HowToUse()

   
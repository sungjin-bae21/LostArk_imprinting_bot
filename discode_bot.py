# -*- coding: utf-8 -*-
"""
 discode 봇 동작
 discode 패키지를 설치하더라도 바로 동작하지 않는다
 python{version}/lib/ 위치로 이동시켜 python 이 discod 모듈을
 인식하도록 한다.
"""


import discord

from user_info import DISCODE_TOKEN

import bot_help
import message_parser
import purchasing_representative


client = discord.Client()
agent = purchasing_representative.PurchasingRepresentative()

@client.event
async def on_ready():
    "클라이언트에 접속되면 호출되는 함수 기본정보를 초기화."
    print('We have logged in as {0.user}'.format(client))
    agent.init_data()


# main
@client.event
async def on_message(message):
    "디스코드 봇으로 메세지가 전달되면 호출되는 함수 실질적인 input 함수"
    if message.author == client.user:
        return

    if message.content.startswith('&&'):
        out_msg = bot_help.OnHelpMessage(message.content)
        await message.channel.send(out_msg)

    if message.content.startswith("::"):
        character_data = message_parser.message_to_character_data(message.content)
        msg = agent.work(character_data)
        await message.channel.send(msg)


client.run(DISCODE_TOKEN)

# -*- coding: utf-8 -*-
"""
 discode 봇 동작
 discode 패키지를 설치하더라도 바로 동작하지 않는다
 python{version}/lib/ 위치로 이동시켜 python 이 discod 모듈을
 인식하도록 한다.
"""

from user_info import DISCODE_TOKEN
import discord

import help
import message_parser
import lost_ark_info
import purchasing_representative

client = discord.Client()
agent = purchasing_representative.PurchasingRepresentative()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# main
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&&'):
        out_msg = help.OnHelpMessage(message.content)
        await message.channel.send(out_msg)

    if message.content.startswith("::"):
        character_data = message_parser.message_to_character_data(message.content)
        agent.work(character_data)
        


client.run(DISCODE_TOKEN)
# -*- coding: utf-8 -*-
"""
 discode 봇 동작
 discode 패키지를 설치하더라도 바로 동작하지 않는다
 python{version}/lib/ 위치로 이동시켜 python 이 discod 모듈을
 인식하도록 한다.
"""

import discord

from lostark_auction_browser import LostArckAuctionBrowser

lostark_action_browser = LostArckAuctionBrowser()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# main
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("")
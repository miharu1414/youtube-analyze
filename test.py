#!/usr/local/bin/python3.7
# coding: utf-8
import json, os, sys, cgi

from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)

from youtuber_search import Youtuber_search

import os
from dotenv import load_dotenv

load_dotenv('.env') 

# API情報

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")



# ボタン生成のための関数
def MakeAction(channel_info):
    return PostbackAction(
        label = channel_info[0],
        display_text = channel_info[0],
        data = channel_info[1]
    )
    
    

text = input("キーワード：")

channels = Youtuber_search(text)

channel = 'which'
    # 飲んでいなければメッセージをプッシュ
buttons_template_message = TemplateSendMessage(
    alt_text='どのチャンネルかな？',
    template=ButtonsTemplate(
        title=channel,
        text='どのチャンネルかな？',
        actions=[MakeAction(channel_info) for channel_info in channels ]
    )
)
# 選択肢ボタンを送信
line_bot_api = LineBotApi(channel_access_token=ACCESS_TOKEN)
line_bot_api.broadcast( buttons_template_message) 


#!/usr/local/bin/python3.7
# coding: utf-8
import json, os, sys, cgi

from youtuber_search import Youtuber_search
from main import main

from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)

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

if os.environ['REQUEST_METHOD'] == 'POST':
  length, _ = cgi.parse_header(os.environ['CONTENT_LENGTH'])
  data = sys.stdin.buffer.read(int(length))

  json_str = data.decode("utf-8")
  json_data = json.loads(json_str)
  sample_dict = json_data

  # webhook接続用
  if len(json_data["events"]) == 0:
    print ("Content-type: application/json\n")
    print ("{}")
    exit()
  

  i = 0
  while True:
    json_path = f'new{i}.json'
    if os.path.exists(json_path):
      i+=1
    else:
      with open( f'new{i}.json', 'w') as f:
        json.dump(sample_dict, f)
      break
  line_bot_api = LineBotApi(channel_access_token=ACCESS_TOKEN)
  USER_ID = str(json_data["events"][0]["source"]["userId"])


# テキストを受信した場合
  if 'message' == json_data["events"][0]["type"]\
    and "text" == json_data["events"][0]["message"]['type']:

    text = json_data["events"][0]["message"]["text"]

    channels = Youtuber_search(text)

    if len(channels) == 0:
      reply = 'すみません |--|\n見つけられませんでした。\n違うワードで検索してみて！'
      line_bot_api.push_message(USER_ID, TextSendMessage(text=reply))
      exit()

    channel = 'どのチャンネルかな？'
        # 飲んでいなければメッセージをプッシュ
    buttons_template_message = TemplateSendMessage(
        alt_text='選択してください',
        template=ButtonsTemplate(
            title=channel,
            text='選択してください',
            actions=[MakeAction(channel_info) for channel_info in channels ]
        )
    )
  # 選択肢ボタンを送信
    line_bot_api = LineBotApi(channel_access_token=ACCESS_TOKEN)
    line_bot_api.push_message(USER_ID, buttons_template_message) 
    exit()


# スタンプの場合
  elif 'message' == json_data["events"][0]["type"]\
    and "sticker" == json_data["events"][0]["message"]['type']:
    reply = "メッセージありがとう。でもスタンプは無理なんだ。。。。"

  # チャンネルidのボタン選択を受信した場合
  elif 'postback' == json_data["events"][0]["type"]:
    channel_id = json_data["events"][0]["postback"]["data"]
   

  if "admin" in reply:
    reply = reply.replace("admin","").lstrip()
    line_bot_api.broadcast(TextSendMessage(text=reply))
  else:
    line_bot_api.push_message(USER_ID, TextSendMessage(text=reply))
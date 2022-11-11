#!/usr/local/bin/python3.7
# coding: utf-8
import json, os, sys, cgi

from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,PostbackAction,ButtonsTemplate)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)


ACCESS_TOKEN = "UzasuxNCBav5Ux2FZ3luOPgscpd3GMEj0mxnBJXJcsgEJCiscsgBH+3uld5yAYLSedDIAIq2K8UztAkw0eQ8vUZHGAEfXG1kZTWWyrb9WcB61Xsh7bdWPJ1AbNmDqzEFVWKnW9PEEJD+2Eq8H21TtwdB04t89/1O/w1cDnyilFU="



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
      with open(json_path, 'w') as f:
        json.dump(sample_dict, f)
      break
  line_bot_api = LineBotApi(channel_access_token=ACCESS_TOKEN)
  USER_ID = str(json_data["events"][0]["source"]["userId"])


# テキストの場合
  if 'message' == json_data["events"][0]["type"]\
    and "text" == json_data["events"][0]["message"]['type']:
      
    text = json_data["events"][0]["message"]["text"]
    reply = ""
    if "筋トレ" in text:
      reply = "最高だよね"
    else:
      reply = text
# スタンプの場合
  elif 'message' == json_data["events"][0]["type"]\
    and "sticker" == json_data["events"][0]["message"]['type']:
    reply = "受信しました。"
    channel = 'which'
        # 飲んでいなければメッセージをプッシュ
    buttons_template_message = TemplateSendMessage(
        alt_text='どのチャンネルかな？',
        template=ButtonsTemplate(
            title=channel,
            text='どのチャンネルかな？',
            actions=[
                PostbackAction(
                    label='ヒカキンTV',
                    display_text='ヒカキンTV',
                    data=f"UCZf__ehlCEBPop-_sldpBUQ"
                ),
                PostbackAction(
                    label='スタジアムオタクのモリチッチ',
                    display_text='スタジアムオタクのモリチッチ',
                    data=f"UCrCuHGz8MkF_ii6JKqbacZA"
                )
            ]
        )
    )
                        #メッセージ送信
    line_bot_api = LineBotApi(channel_access_token=ACCESS_TOKEN)
    line_bot_api.push_message(USER_ID, buttons_template_message) 
  elif 'postback' == json_data["events"][0]["type"]:
    text = json_data["events"][0]["postback"]["data"]
    reply = "https://www.youtube.com/channel/" + str(text)

   

  if "admin" in reply:
    reply = reply.replace("admin","").lstrip()
    line_bot_api.broadcast(TextSendMessage(text=reply))
  else:
    line_bot_api.push_message(USER_ID, TextSendMessage(text=reply))


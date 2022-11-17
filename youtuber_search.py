from apiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv('.env') 

# API情報
API_KEY = os.environ.get("Youtube_API_KEY")
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def Youtuber_search(key_word):
    try:
        youtube = build(
            YOUTUBE_API_SERVICE_NAME, 
            YOUTUBE_API_VERSION,
            developerKey=API_KEY
            )

        search_response = youtube.search().list(
        q='['+key_word+']',
        part='id,snippet',
        maxResults=25
        ).execute()

        channels = []
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#channel":
                channels.append([search_result["snippet"]["title"],
                                        search_result["id"]["channelId"]])
    except:
        API_KEY = os.environ.get("Youtube_API_KEY1")
        youtube = build(
            YOUTUBE_API_SERVICE_NAME, 
            YOUTUBE_API_VERSION,
            developerKey=API_KEY
            )

        search_response = youtube.search().list(
        q='['+key_word+']',
        part='id,snippet',
        maxResults=25
        ).execute()

        channels = []
        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#channel":
                channels.append([search_result["snippet"]["title"],
                                        search_result["id"]["channelId"]])

    return channels

if __name__ == '__main__':
    key_word = input("キーワード：")
    channels = Youtuber_search(key_word)
    for channel in channels:
        print(channel)
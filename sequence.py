from telnetlib import DO
from miharu.sample_comment import Make_comment_table,Movie2text
from igaiga.movie_download import Download_movie,all_data_get,movie_to_jpg

import pandas as pd

CHANNEL_ID = ""

def main(channel_id,num=5):
    print("チャンネル情報を収集します。")
    all_data_get(channel_id)
    
    
    
    print("動画情報の取得を始めます。")
    
    # コメントのダウンロード
    try:
        Make_comment_table(video_id)
        print("コメントのダウンロードが完成しました。")
    except:
        print("コメントのダウンロードができませんでした。")
        
    # 動画のダウンロード
    try:
        print('動画のダウンロードを始めます')
        Download_movie(video_id)
        print("完了")
    except:
        print("動画のダウンロードに失敗しました。")

if __name__ == '__main__':
    CHANNEL_ID = input("チャンネルid:")
    main(CHANNEL_ID)
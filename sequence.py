from telnetlib import DO
from functions_youtube.sample_comment import Make_comment_table
from functions_youtube.text_generate import Movie2text
from functions_youtube.mkdir import Make_dir
from functions_youtube.movie_download import Download_movie
from functions_youtube.all_data import all_data_get
from functions_youtube.movie_to_jpg import movie_to_jpg

import pandas as pd

CHANNEL_ID = "UCrCuHGz8MkF_ii6JKqbacZA"

def main(channel_id,num=3):
    print("チャンネル情報を収集します。")
    
    # Channel_idの各フォルダーを作成
    Make_dir(channel_id)
    
    # Channelの各動画情報を取得し、excel化
    all_data_get(channel_id)
    
    #各動画情報をデータフレームで取得する
    df = pd.read_excel(f'igaiga_data/{channel_id}/info/data_{channel_id}.xlsx', index_col=None)
    #video_idをリスト化
    Video_ids = list(df['id'])
    
    print("動画情報の取得を始めます。")
    
    for video_id in Video_ids:
        # コメントのダウンロード
        try:
            Make_comment_table(channel_id,video_id)
            print("コメントのダウンロードが完成しました。")
        except:
            print("コメントのダウンロードができませんでした。")
            
        # 動画のダウンロード
        try:
            print('動画のダウンロードを始めます')
            Download_movie(channel_id,video_id)
            print("完了")
        except:
            print("動画のダウンロードに失敗しました。")

if __name__ == '__main__':
    CHANNEL_ID = input("チャンネルid:")
    main(CHANNEL_ID)
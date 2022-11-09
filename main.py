from telnetlib import DO
from miharu.sample_comment import Make_comment_table
from igaiga.movie_download import Download_movie
from igaiga.all_data import all_data_get
VIDEO_ID = "gnIOzY7esA0"
video_id = VIDEO_ID
print("動画情報の取得を始めます。")
channel_id = 'UCrCuHGz8MkF_ii6JKqbacZA'
all_data_get(channel_id)


"""
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
"""
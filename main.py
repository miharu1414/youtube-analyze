from telnetlib import DO
from miharu.sample_comment import Make_comment_table
from igaiga.movie_download import Download_movie

VIDEO_ID = "gnIOzY7esA0"
video_id = VIDEO_ID
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
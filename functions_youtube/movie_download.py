
from yt_dlp import YoutubeDL

VIDEO_ID = 'gnIOzY7esA0'



#igaiga_data → dataに，sample → channel_id直す
def Download_movie(channel_id, video_id):
    movie_url = "https://www.youtube.com/watch?v="+video_id
    ydl_opts = {'format':'best','outtmpl':f"igaiga_data/{channel_id}/movie/"+video_id+'.%(ext)s',}
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

if __name__ == '__main__':
    Download_movie(VIDEO_ID)

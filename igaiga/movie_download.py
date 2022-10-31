from __future__ import unicode_literals
import youtube_dl

VIDEO_ID = 'gnIOzY7esA0'

#igaiga_data → dataに，sample → channel_id直す
def Download_movie(channel_id, video_id):
    movie_url = "https://www.youtube.com/watch?v="+video_id
    ydl_opts = {'outtmpl':"igaiga_data/sample/movie/"+video_id+".mp4",}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([movie_url])

if __name__ == '__main__':
    Download_movie(VIDEO_ID)

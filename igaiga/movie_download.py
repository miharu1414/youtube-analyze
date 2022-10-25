from __future__ import unicode_literals
import youtube_dl

VIDEO_ID = 'gnIOzY7esA0'

def Download_movie(video_id):
    movie_url = "https://www.youtube.com/watch?v="+video_id
    ydl_opts = {'outtmpl':"data/movie/"+video_id,}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([movie_url])

if __name__ == '__main__':
    Download_movie(VIDEO_ID)
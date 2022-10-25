from __future__ import unicode_literals
import youtube_dl


def movie(movie_url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([movie_url])
    


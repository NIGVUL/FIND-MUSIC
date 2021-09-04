from youtubesearchpython import VideosSearch
from youtube_dl import YoutubeDL
import os
from easygui import enterbox
from time import sleep

def searchYouTube():
    text = enterbox('Введите песню: ', 'Поиск песни')
    if 'time.webm' in os.listdir() :
        os.remove('time.webm')

    elif 'time.m4a' in os.listdir() :
        os.remove('time.m4a')


    videosSearch = VideosSearch(text, limit=1).result()
    title = videosSearch['result'][0]['title']
    url = videosSearch['result'][0]['link']
    print(url)
    try:
        ydl_opts = {
            'outtmpl': 'time.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            ]
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        pass

    sleep(2)
    if 'time.webm' in os.listdir() :
        os.system('start time.webm')

    elif 'time.m4a' in os.listdir() :
        os.system('start time.m4a')




searchYouTube()






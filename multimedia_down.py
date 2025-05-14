import os
import re
import traceback

##-------------------------------youtube, movie start
import yt_dlp
##-------------------------------youtube, movie end

##-------------------------------image start
import requests
from selenium import webdriver
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('headless')
##-------------------------------image end

def movie_down(URL, target='movie'):
    if target == "music":
        ydl_opts = {
            'format': 'bestaudio',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}]
        }
    else:
        ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',  # 저장할 파일 이름 형식
            'format': 'bestvideo+bestaudio/best',  # 최고 화질/음질 조합
            'merge_output_format': 'mp4',  # 비디오와 오디오 병합 포맷
            'writesubtitles': True, 'subtitleslangs': ['ko'] # 한글 자막 있으면 자막 포함
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])


def image_down(URL):
    response = requests.get(URL)

    if response.status_code == 200:
        html = response.text
        bs = BeautifulSoup(html, 'html.parser')
        print(bs)

        a = bs.findAll('img')
        for i in range(len(a)):
            b = a[i].attrs['src']
            b = "https:" + b
            print(b)
            try:
                urlretrieve(b, '{}.jpg'.format(i))
            except:
                print("err : ", b)

    else:
        print(response.status_code)

def main(target = "", URL = ""):
    if(target == "" and URL == ""):
        target = input("target : ")
        URL = input("URL : ")

    try:
        if target == "image":
            image_down(URL)
        elif target == "movie":
            movie_down(URL)
        elif target == "music":
            movie_down(URL,target)
    except:
        traceback.print_exc()
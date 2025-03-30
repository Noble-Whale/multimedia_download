import os
import re
import traceback

##-------------------------------youtube, movie start
import pytubefix # youtube에서 로직 및 파라미터를 계속 패치하는 것 같은데, 안되면 pip install pytubefix --upgrade로 최신버전 받아볼 것
from moviepy import *
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
    yt = pytubefix.YouTube

    video_content = yt(URL, "WEB") # nodejs 필요, python interpreter 3.13 ↑

    print(video_content.title)

    video = video_content.streams.get_highest_resolution()

    yt_filename = re.sub("(/|\.mp4)", "", video.default_filename) # ①파일 이름에 /가 들어가면 경로로 인식해서 moviepy가 오류를 떨궈서 문자 대체
                                                                            # ②확장자(.mp4)를 빼서 순수한 파일명만 추출

    os.rename(video.download(), yt_filename + ".mp4") # 다운로드 하고, 완료된 파일의 파일명도 변경함

    if target == "music":
        mvpy_video = VideoFileClip(yt_filename + ".mp4")
        mvpy_video.audio.write_audiofile(yt_filename + ".mp3")


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
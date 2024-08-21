##-------------------------------youtube, movie start
import pytube #old
import pytubefix
from moviepy.editor import *
##-------------------------------youtube, movie end

##-------------------------------image start
import requests
from selenium import webdriver
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
options = webdriver.ChromeOptions()
options.add_argument('headless')
##-------------------------------image end

def movie_down(URL, target='movie'):
    yt = pytube.YouTube  # old
    yt2 = pytubefix.YouTube

    video = yt2(URL).streams.get_highest_resolution()
    video.download()

    if target == "music":
        mvpy_video = VideoFileClip(video.default_filename)
        mvpy_video.audio.write_audiofile(video.default_filename + ".mp3")


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


target = input("target : ")
URL = input("URL : ")

if target == "image":
    image_down(URL)
elif target == "movie":
    movie_down(URL)
elif target == "music":
    movie_down(URL,target)
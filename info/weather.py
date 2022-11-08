#Python Korea Weather Crawling 2022 Revise
#https://mustzee.tistory.com

import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
#1번 파일이 실행될 때 환경변수에 현재 자신의 프로젝트의 settings.py파일 경로를 등록.
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","[프로젝트이름].settings")
 
#2번 실행파일에 Django 환경을 불러오는 작업.
import django
django.setup()

from .models import weather


def getWeather():
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8')

    soup = BeautifulSoup(webpage, 'html.parser')
    temps = soup.find('div','temperature_text')

    #test
    a  = temps.text.strip()[5:]
    #print(a)
    return a

# if __name__ == '__main__':
#     result = getWeather()
#     print(result)

a = getWeather()

weather(weather=a).save()
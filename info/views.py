from django.shortcuts import render
import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
from .models import Sensor

# Create your views here.
from django.shortcuts import render
from .weather import getWeather

# def mycar(request):
# #    weatherinfo = getWeather()
# 	return render(request, 'info/mycar.html')

def animation_car(request):
    return render(request, 'info/animation_car.html')

def mycar(request):
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8')

    soup = BeautifulSoup(webpage, 'html.parser')
    temps = soup.find('div','temperature_text')
    status = soup.find('span', 'weather before_slash')

    #DB에서 수위 조절 센서 테이블 객체 모두 불러오기
    sensorValues = Sensor.objects.all()

    #test
    a  = temps.text.strip()[5:]
    b = status.text.strip()
    #print(a)
    #print(b)
    return render(request, 'info/mycar.html', {"sensorValues": sensorValues, 'weather':a, 'status':b})

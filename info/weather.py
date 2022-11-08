import datetime
import urllib
from bs4 import BeautifulSoup
import urllib.request as req
 

def getWeather():
    webpage = urllib.request.urlopen('https://search.naver.com/search.naver?query=%EB%82%A0%EC%94%A8')

    soup = BeautifulSoup(webpage, 'html.parser')
    temps = soup.find('div','temperature_text')
    status = soup.find('span', 'weather before_slash')
    #test
    a  = temps.text.strip()[5:]
    b = status.text.strip()
    print(a)
    print(b)



    #print(a)
    return a


getWeather()



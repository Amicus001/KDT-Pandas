#from modulename import*
#modulename 내의 모든 변수, 함수, 클래스 가져오기.
#모듈 내의 변수/함수/클래스 사용 시 모듈 호출 불필요

import urllib.request as req
from http.client import HTTPResponse
dataObj = req.urlopen('https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
from urllib import error, parse
print (dataObj)
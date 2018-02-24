from bs4 import BeautifulSoup
import urllib
from selenium import webdriver
import time

start_time = time.time()

base = 'www.seloger.com/'
url = 'http://' + base + 'list.htm?idtt=2&div=2238'
urlannonce = []
f = open('seloger_Adsurls.txt', 'r')
for line in f:
    urlannonce.append(line.replace('\n',''))

urls = [url]
visited = [url]
f2 = open('seloger_Adsurls.txt', 'a')

browser = webdriver.Chrome("D:\chromedriver.exe") 
i=1
while len(urls)>0:
    
    browser.get(urls[0])
    print('Url en cours : '+ str(urls[0]))
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    
    i+=1
f2.close()
browser.close()
print("--- %s seconds ---" % (time.time() - start_time))

        
        
        
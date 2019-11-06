# -*- coding: utf-8 -*-
import urllib.request
import re
import time

from selenium import webdriver

def downloadPinterestImages():
    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

    link="https://gr.pinterest.com/pin/288934132334754326/"
    browser.get(link)

    time.sleep(2)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    limit=7 #limit of scrolls
    while(match==False and limit>0): #auto scroll till end or till limit
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        limit = limit-1;
        if lastCount==lenOfPage:
            print("stop scrolling")
            match=True
        else:
            print("scrolling..")

    response = browser.page_source#.encode(encoding='UTF-8')

    toDel =[]
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response)

    print(len(urls))
    for i in range(len(urls)):
        if(urls[i][-4:]==".jpg"):
            urls[i]=re.sub('.com/.*?/','.com/originals/',urls[i],flags=re.DOTALL)
        else:
            urls[i]= ""

    urls = list(set(urls))

    urls = list(filter(None, urls)) # fastest
    urls = list(filter(bool, urls)) # fastest
    urls = list(filter(len, urls))  # a bit slower

    with open('raw.txt', 'w') as f:
        for url in urls:
            f.write("%s\n" % url)
    f.close()

    for i in range(len(urls)):
        try:
            urllib.request.urlretrieve(urls[i], "images/"+str(i)+"-image.jpg")
        except:
            print("Broken Link") 
        
        

downloadPinterestImages()

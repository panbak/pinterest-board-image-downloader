    import pprint
    import requests
    import urllib
    import re
    import time

    from selenium import webdriver


    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

    link=raw_input("Paste Board Link:") 
    browser.get(link)

    time.sleep(2)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            print("stop scrolling")
            match=True
        else:
            print("scrolling..")

    response = browser.page_source.encode(encoding='UTF-8')

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
        urllib.urlretrieve(urls[i], "images/"+str(i)+"-image.jpg")



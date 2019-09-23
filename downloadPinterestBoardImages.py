    import urllib
    import re
    import time

    from selenium import webdriver


    browser = webdriver.Firefox(executable_path=r'geckodriver.exe')

    link="pinterest board lik" #the pinterest board link
    browser.get(link)

    time.sleep(2)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    limit=7 #limit of scrolls
    while(match==False and limit>0): #auto scroll till end or till limit
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            print("stop scrolling")
            match=True
        else:
            print("scrolling..")

    response = browser.page_source.encode(encoding='UTF-8')

    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response)

    print(len(urls))
    for i in range(len(urls)):
        if(urls[i][-4:]==".jpg"):
            urls[i]=re.sub('.com/.*?/','.com/originals/',urls[i],flags=re.DOTALL)
        else:
            urls[i]= ""

    urls = list(set(urls))#remove duplicates

    urls = list(filter(None, urls)) 
    urls = list(filter(bool, urls))
    urls = list(filter(len, urls)) 

    with open('raw.txt', 'w') as f: #writes the image links in a txt file
        for url in urls:
            f.write("%s\n" % url)
    f.close()

    for i in range(len(urls)):#save images 
        urllib.urlretrieve(urls[i], "images/"+str(i)+"-image.jpg")



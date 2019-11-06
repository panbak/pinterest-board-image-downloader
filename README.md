# pinterest-board-image-downloader
A python script that downloads all images of a pinterest board.
Written in Python 3

The script collects all the urls of the page and after that it filters the url list to keep only the pins( .jpg images )

Dependencies: 
  1.  selenium (pip install selenium)
  
Selenium uses firefox to work so it needs firefox installed and geckodriver: https://github.com/mozilla/geckodriver/releases. Download and extract geckodriver.exe file in the same folder with downloadPinterestBoardImages.py.
Also make a folder named 'images' to save the downloaded pinterest pins.

If you want to use another browser such as Chrome, check selenium docs: https://selenium-python.readthedocs.io/installation.html

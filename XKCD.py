
#Heres what your program does:
#Loads the XKCD home page.
#Saves the comic image on that page.
#Follows the Previous Comic link.
#Repeats until it reaches the first comic.

#Step 1 - Get the website using requests module
#Step 2 - Get the comic and save to a temp directory
#Step 3 - Go to previous link
#Step 4 - Repeat Step 2 until no previous link exists



#Step 1

import requests
from bs4 import BeautifulSoup
import os

response = requests.get('https://xkcd.com/')
try:
    response.raise_for_status()
    soup = BeautifulSoup(response.content,'html.parser')
    comic = soup.select("#comic img")
    if comic != []:
        currentComicUrl = r'http:'+comic[0].get("src")
        print "Downloading http:"+comic[0].get("src")
        imageReq = requests.get(currentComicUrl)
        imageFile = open(os.path.join('D:\Python', os.path.basename(currentComicUrl)), 'wb')
        for chunk in imageReq.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        prevLink = soup.select("a[rel='prev']")[0]
        print prevLink.get('href')
except Exception as exc:
    print exc


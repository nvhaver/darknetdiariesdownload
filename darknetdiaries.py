# Darknet diaries download script

# install dependencies with the command:
# pip install urllib shutil beautifulsoup4

import re
import urllib.request
import shutil
from bs4 import BeautifulSoup

episodes = 47
r = r'"mp3": "(.*\.mp3)'
directory = 'D:/Test/' # Change this to your destination folder (don't forget the trailing /)

for episode in range(episodes):
    url = "https://darknetdiaries.com/episode/"+str(episode+1)
	# Default UA is blocked
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find('article')
    script = article.find('script')  
    link = re.search(r, str(script))

    with urllib.request.urlopen(link.group(1)) as response, open(directory + 'darknet-diaries-ep'+str(episode+1)+'.mp3', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
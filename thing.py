import re
from urllib.parse import urlparse

 
all = []
with open("jukebox.txt") as file:
        for line in file:
            urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", line)
            all.extend(urls)

#print(all)
spotify_links = []
for url in all:
    about = urlparse(url)
    if(about.netloc == "open.spotify.com"):
        data = about.path.split("/")
        print(data)

#print(spotify_links)
import re
from urllib.parse import urlparse

import spotipy
import spotipy.util as util
 
all = []
with open("jukebox.txt") as file:
        for line in file:
            urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", line)
            all.extend(urls)

#print(all)
track_list = []
for url in all:
    about = urlparse(url)
    if(about.netloc == "open.spotify.com"):
        data = about.path.split("/")
        if(data[1]=='track'):
            track_list.append(data[2])

#print(spotify_links)
print(track_list)
print(len(track_list))

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

i=0
for trax in chunks(track_list,50):
    with open('tracks%s.txt'% str(i), 'w') as f:
        for item in trax:
            f.write("spotify:track:%s," % item)
    i=i+1
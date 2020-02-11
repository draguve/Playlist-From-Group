import re
from urllib.parse import urlparse,parse_qsl

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
 
all = []
with open("jukebox.txt") as file:
    for line in file:
        urls = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", line)
        all.extend(urls)


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client.json"

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

def add_vid(id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
          "snippet": {
            "playlistId": "PLkC1ELgs_K3-P-_EnufZ5FiRAuH6vfvyi",
            "position": 0,
            "resourceId": {
              "kind": "youtube#video",
              "videoId": id
            }
          }
        }
    )
    response = request.execute()
    return response

with open('resp.txt', 'w') as f:
    type_of_links = []
    links = []
    small = []
    for url in all:
        try:
            about = urlparse(url)
            if(about.netloc in ['www.youtube.com','m.youtube.com']):
                if(about.path=='/watch'):
                    data = parse_qsl(about.query)
                    response = add_vid(data[0][1])
                    f.write(str(response))
            if(about.netloc == 'youtu.be'):
                response = add_vid(about.path[1:])
                f.write(str(response))
        except Exception as inst:
            print("Problem in "+ url + " " + str(type(inst)))
            f.write("Problem in "+ url)
   
        
    

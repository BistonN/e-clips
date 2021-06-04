# from crawler_clips_twitch import VideoTwitch
import pandas as pd
from google_services import Create_Service
from googleapiclient.http import MediaFileUpload
from datetime import datetime
from crawler_clips_twitch import VideoTwitch

VideoTwitch()

# CLIENT_SECRET_FILE = './credentials/client_secret.json'
# API_NAME = 'youtube'
# API_VERSION = 'v3'
# SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# upload_date_time = datetime(2021, 5, 9, 0, 0, 0).isoformat() + '.000Z'

# request_body = {
#     'snippet': {
#         'categoryI': 19,
#         'title': 'Upload Testing',
#         'description': 'Hello World Description',
#         'tags': ['Travel', 'video test', 'Travel Tips']
#     },
#     'status': {
#         'privacyStatus': 'public',
#         'selfDeclaredMadeForKids': False, 
#     },
#     'notifySubscribers': True
# }

# mediaFile = MediaFileUpload('./clips/{}/{}-conc.mp4'.format(video_name, video_name))

# response_upload = service.videos().insert(
#     part='snippet,status',
#     body=request_body,
#     media_body=mediaFile
# ).execute()

# service.thumbnails().set(
#     videoId=response_upload.get('id'),
#     media_body=MediaFileUpload('thumbnail.png')
# ).execute()
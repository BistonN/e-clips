# from crawler_clips_twitch import VideoTwitch
import pandas as pd
from google_services import Create_Service, convert_to_RFC_datetime
from googleapiclient.http import MediaFileUpload
from datetime import datetime

CLIENT_SECRET_FILE = './credentials/client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
upload_date_time = datetime.utcnow().isoformat() + 'Z'

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': 'Upload Testing',
        'description': 'Hello World Description',
        'tags': ['Travel', 'video test', 'Travel Tips']
    },
    'status': {
        'privacyStatus': 'public',
        'publishAt': upload_date_time,
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': True
}

mediaFile = MediaFileUpload('./clips/my_concatenation.mp4')

# videotwitch = VideoTwitch()

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

# service.thumbnails().set(
#     videoId=response_upload.get('id'),
#     media_body=MediaFileUpload('thumbnail.png')
# ).execute()
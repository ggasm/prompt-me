import os
from apiclient.discovery import build

from suggestion import Suggestion
from typing import List
from resource import Resource


class Youtube(Resource):
    def lookup(self, keyword: str) -> List[Suggestion]:
        api_key = os.environ.get('ICHACK_YT_APIKEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(q=keyword, part='snippet', type='video')
        result = request.execute()
        all_videos = result['items']
        return [Suggestion('https://www.youtube.com/watch?v=' + video['id']['videoId'],
                video['snippet']['title'], video['snippet']['channelTitle']) for video in all_videos]
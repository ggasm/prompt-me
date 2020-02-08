import json
import os

from suggestion import Suggestion
from typing import List
from resource import Resource
import requests


class NewsApi(Resource):    
    def lookup(self, keyword: str, maxResults: int = 3) -> List[Suggestion]:
        api_key = os.environ.get('ICHACK_NEWS_APIKEY')
        parameters = {
            'q': keyword,
            'pagesize': 100,
            'apiKey': api_key,
            'language': 'en',
            'sortBy': 'popularity',
        }
        response = requests.get('https://newsapi.org/v2/everything', parameters)
        response_dict = response.json()
        suggestions = []
        i = 0
        for article in response_dict['articles']:
            if i >= maxResults:
                break
            suggestions.append(Suggestion(article['url'], article['description'], article['author']))
            i += 1
        return suggestions
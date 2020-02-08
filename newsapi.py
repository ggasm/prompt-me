import json

from suggestion import Suggestion
from typing import List
from resource import Resource
import requests


class NewsApi(Resource):

    def lookup(self, keyword: str) -> List[Suggestion]:
        api_key = "750565b602914552ac29ea23d3e4e4f5"

        parameters = {
            'q': keyword,
            'pagesize': 100,
            'apiKey': api_key,
            'language': 'en',
            'sortBy': 'popularity',
        }

        response = requests.get('https://newsapi.org/v2/everything', parameters)

        response_dict = json.loads(response);

        suggestions = []

        for i in response_dict['articles']:
            suggestions.append([i['url'], i['description'], i['author']])


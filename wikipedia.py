import requests

from suggestion import Suggestion
from typing import List
from resource import Resource


class Wikipedia(Resource):
    URL = 'https://en.wikipedia.org/w/api.php'
    limit = 3
    parameters = { 'action': 'opensearch', 'format': 'json', 'limit' : str(limit) }

    def lookup(self, keyword: str) -> List[Suggestion]:
        self.parameters['search'] = keyword
        search = requests.Session()
        response = search.get(url=self.URL, params=self.parameters)
        results = response.json()
        urls = results[1]
        titles = results[3]
        suggestions = []
        i = 0
        for _ in urls:
            if i >= self.limit:
                break
            suggestion = Suggestion(titles[i], urls[i], None)
            suggestions.append(suggestion)
            i += 1
        return suggestions
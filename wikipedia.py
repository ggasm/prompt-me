<<<<<<< HEAD
from dataclasses import dataclass
=======
import requests
>>>>>>> f0e3f09d0fa749d86fdebc3f0f9a9db8496fe2af

from suggestion import Suggestion
from typing import List
from resource import Resource


class Wikipedia(Resource):
    URL = 'https://en.wikipedia.org/w/api.php'
    parameters = { 'action': 'opensearch', 'format': 'json' }

    def lookup(self, keyword: str, maxResults: int = 3) -> List[Suggestion]:
        self.parameters['search'] = keyword
        self.parameters['limit'] = maxResults
        search = requests.Session()
        response = search.get(url=self.URL, params=self.parameters)
        results = response.json()
        urls = results[1]
        titles = results[3]
        suggestions = []
        i = 0
        for _ in urls:
            if i >= maxResults:
                break
            suggestion = Suggestion(titles[i], urls[i], None)
            suggestions.append(suggestion)
            i += 1
        return suggestions


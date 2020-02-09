from typing import List

import requests

from resource import Resource
from suggestion import Suggestion


class BooksApi(Resource):

    def lookup(self, keyword: str, maxResults: int = 3) -> List[Suggestion]:

        # not printing more than 1 result
        parameters = {
            'q': keyword,
            'langRestrict': 'en',
            'orderBy': 'relevance',
            'access_token': 'oauth2-token',
        }

        get_response = requests.get('https://www.googleapis.com/books/v1/volumes?', parameters)
        responses = get_response.json()

        suggestions = []
        i = 0

        for response in responses['items']:
            authors_suggestion = ""
            authors = response['volumeInfo']['authors']
            for author in authors:
                if authors_suggestion == '':
                    authors_suggestion += author
                else:
                    authors_suggestion += ", " + author
            if authors_suggestion == "":
                authors_suggestion = 'no authors found'
            suggestions.append(Suggestion((response['volumeInfo']).get("previewLink", 0),
                                          (response['volumeInfo']).get("title", 0) + ': ' + (
                                              response['volumeInfo']).get(
                                              "title", 0),
                                          authors_suggestion))
            i += 1
        return suggestions

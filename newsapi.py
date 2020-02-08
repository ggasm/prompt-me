from suggestion import Suggestion
from typing import List
from resource import Resource


class NewsApi(Resource):
    def lookup(self, keyword: str) -> List[Suggestion]:
        super().lookup(keyword)
        print("from class")
        pass

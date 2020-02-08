from suggestion import Suggestion
from typing import List
from resource import Resource


class Wikipedia(Resource):
    def lookup(self, keyword: str) -> List[Suggestion]:
        return super().lookup(keyword)


from typing import List
from abc import ABC

from suggestion import Suggestion


class Resource(ABC):
    def lookup(self, keyword: str) -> List[Suggestion]:
        print(f"looking up keyword: {type(self)}:{keyword}")
        pass


from typing import List
from abc import ABC

from suggestion import Suggestion


class Resource(ABC):
    def get_name(self):
        return self.__class__.__name__

    def lookup(self, keyword: str) -> List[Suggestion]:
        print(f"looking up keyword: {self.get_name()}:{keyword}")

        return [Suggestion("www.dummyurl.com", "Dummy description", "dummy author")]

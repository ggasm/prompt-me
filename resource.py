from dataclasses import dataclass
from typing import List

from suggestion import Suggestion


@dataclass(frozen=True)
class Resource:

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return str(self)

    def lookup(self, keyword: str) -> List[Suggestion]:
        print(f"looking up keyword: {self}:{keyword}")

        return [Suggestion("www.dummyurl.com", "Dummy description", "dummy author")]

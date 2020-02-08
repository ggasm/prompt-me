from dataclasses import dataclass


@dataclass
class Suggestion:
    url: str
    description: str
    author: str

import pke
from typing import List


class KeywordExtractor:
    valid_pos = {'NOUN', 'PROPN', 'ADJ'}

    def __init__(self):
        self.extractor = pke.unsupervised.SingleRank()

    def extract_hot_keywords(self, text: str, n_best: int) -> List[str]:
        self.extractor.load_document(input=text, language='en', normalization=None)
        self.extractor.candidate_selection(pos=self.valid_pos)
        self.extractor.candidate_weighting(window=10, pos=self.valid_pos)

        return [word for (word, _) in self.extractor.get_n_best(n=n_best)]

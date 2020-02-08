import pke
import json


class KeyphraseReader:
    kp_sets = []

    def __init__(self, json_file, ctx_id):
        with open(json_file) as json_data:
            data = json.load(json_data)
        self.contexts = data[ctx_id]

    def get_keyphrase_sets(self, n):
        if self.kp_sets == []:
            valid_pos = {'NOUN', 'PROPN', 'ADJ'}
            for context in self.contexts:
                extractor = pke.unsupervised.SingleRank()
                extractor.load_document(input=context, language='en', normalization=None)
                extractor.candidate_selection(pos=valid_pos)
                extractor.candidate_weighting(window=10, pos=valid_pos)
                kp_tups = extractor.get_n_best(n=n)
                kp_set = []
                for kp_tup in kp_tups:
                    kp_set.append(kp_tup[0])
                self.kp_sets.append(kp_set)
            return self.kp_sets
        else:
            return self.kp_sets

    def get_keyphrase_set(self, n, i):
        if self.kp_sets == []:
            return self.get_keyphrase_sets(n)[i]
        else:
            return self.kp_sets[i]

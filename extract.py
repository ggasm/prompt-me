import pke
import json


class KeyphraseReader:
    def __init__(self, json_file, ctx_id):
        with open(json_file) as json_data:
            data = json.load(json_data)
        self.contexts = data[ctx_id]

    def get_keyphrase_set(self, ctx_i, n):
        valid_pos = {'NOUN', 'PROPN', 'ADJ'}
        extractor = pke.unsupervised.SingleRank()
        extractor.load_document(input=self.contexts[ctx_i], language='en', normalization=None)
        extractor.candidate_selection(pos=valid_pos)
        extractor.candidate_weighting(window=10, pos=valid_pos)
    
        kp_tups = extractor.get_n_best(n=n)
        kp_set = []
        for kp_tup in kp_tups:
            kp_set.append(kp_tup[0])
        return kp_set

if __name__ == "__main__":
    reader = KeyphraseReader('contexts.json','contexts')
    print(reader.get_keyphrase_set(0, 3))
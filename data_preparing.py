from nltk.tokenize import sent_tokenize, RegexpTokenizer
from nltk import pos_tag
from data_cleansing import Entry
import json


example = """ <id>http://arxiv.org/abs/physics/0303043v1</id>
    <updated>2003-03-11T08:53:41Z</updated>
    <published>2003-03-11T08:53:41Z</published>
    <title>Geometric phase due to helicity inversion of photons inside an optical
  fiber composed periodically of left- and right- handed media</title>
    <summary>  In this Letter, it is claimed that, in addition to the Chiao-Wu geometric
phase and optical Aharonov-Carmi geometric phase, there exists a new
interesting geometric phase caused by the helicity inversion of photons in the
optical fiber composed periodically of left- and right- handed (LRH) media. By
making use of the Lewis-Riesenfeld invariant theory and the invariant-related
unitary transformation formulation, we calculate this geometric phase. It is
emphasized that this geometric phase should not been neglected when considering
the anomalous refraction on the interfaces between left- and right- handed
media.
</summary>
    <author>
      <name>Jian Qi Shen</name>
    </author>
    <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom">5 pages, Latex</arxiv:comment>
    <link href="http://arxiv.org/abs/physics/0303043v1" rel="alternate" type="text/html"/>
    <link title="pdf" href="http://arxiv.org/pdf/physics/0303043v1" rel="related" type="application/pdf"/>
    <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom" term="physics.optics" scheme="http://arxiv.org/schemas/atom"/>
    <category term="physics.optics" scheme="http://arxiv.org/schemas/atom"/>
    <category term="physics.gen-ph" scheme="http://arxiv.org/schemas/atom"/>"""


word_tokenizer = RegexpTokenizer(r'\w(?:[-\w]*\w)?')
NOUN_TYPES = ('NN','NNS','NNP','NNPS')


def merge_adjacent_components_of_same_type(sent_components):
    prev = None
    merged = []
    for w, t in sent_components:
        if prev in NOUN_TYPES and t in NOUN_TYPES:
            last = merged[-1]
            new_word = last[0] + '_' + w
            merged[-1] = (new_word, t)

        elif prev == 'JJ' and t in NOUN_TYPES:
            last = merged[-1]

            new_word = last[0] + '_' + w
            merged[-1] = (new_word, t)

        else:
            merged.append((w,t))

        prev = t

    return merged


def prepare_document(text):
    nouns = []
    for sent in sent_tokenize(text):
        words = word_tokenizer.tokenize(sent)
        # in between processing
        # ************************************** #
        words = [w.lower() for w in words]
        # ************************************** #
        sent_components = pos_tag(words)

        for(w, t) in merge_adjacent_components_of_same_type(sent_components):
            if t in ('NN', 'NNS', 'NNP', 'NNPS'):
                nouns.append(w)
    return nouns


if __name__ == '__main__':
    sample = json.load(open('arxiv_sample.json'))
    for i in range(10):
        summary = sample[i]['summary']
        print(summary)
        print(prepare_document(summary))




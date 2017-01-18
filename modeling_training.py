import json
from gensim import corpora
from gensim.models.wrappers.ldamallet import LdaMallet
from multiprocessing import cpu_count

MALLET_PATH='/usr/local/Cellar/mallet/2.0.7/bin/mallet'

if __name__ == '__main__':
    lst = json.load(open('.json'))
    # constructing a document-term matrix
    dictionary = corpora.Dictionary(lst)
    dictionary.filter_extremes(20, 0.1)



    # # print(dictionary)
    corpus = [dictionary.doc2bow(x) for x in lst]
    # print(corpus)

    lda = LdaMallet(
        mallet_path=MALLET_PATH,
        corpus=corpus,
        id2word=dictionary,
        num_topics=30,
        optimize_interval=10,
        iterations=2000,
        workers=cpu_count(),
    )

    lda.save('dnc_mallet')

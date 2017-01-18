import json
from data_cleansing import Entry
from preprocessing import preprocess_document, Pool



if __name__ == '__main__':
    lst = json.load(open('arxiv_2000_2016.json'))
    all_entries = [Entry(x) for x in lst]
    for y in range(2000, 2017):
        entries_at_y = [x.summary for x in all_entries if x.published.year==y]
        print(y,":", len(entries_at_y))
        json.dump(entries_at_y, open('text_{}.json'.format(y), 'w'))


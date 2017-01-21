from topic_chain import *
from extract_tree import *

class VisLineFormat:

    """
    lines: list<list<DynamicTopic>>
    """

    def __init__(self, lines, labels):
        self._lines = lines
        self._labels = labels

    def convert_line_to_json(self, at):
        labels = self._labels
        topics = self._lines[at]
        lst = []
        line = {'topics':lst, 'words':None}

        for t in topics:
            sublst = []
            sublst.append(labels[t.ts]) # add label
            sublst.append(str(t.ts) + str(t.ti)) #positional index
            sublst.append(3000) # popularity
            sublst.append([(p, w) for w, p in t.top_word_distribution(20)])
            lst.append(sublst)
        # add in the pointer
        if len(topics[-1].next()):
            pointer_topic = topics[-1].next()[0]
            sublst = []
            sublst.append(labels[pointer_topic.ts])
            sublst.append(str(pointer_topic.ts) + str(pointer_topic.ti))
            sublst.append(' ')
            lst.append(sublst)

        common_words = DynamicTopic.common_words(topics, 10)
        line['words'] = ' '.join(common_words)
        return json.dumps(line)

    def to_json_lst(self):
        lst = []
        for i in range(len(self._lines)):
            json_str = self.convert_line_to_json(i)
            lst.append(json_str)
        return lst


if __name__ == '__main__':
    tc = TopicChain('topic_keys.json', threshold=0.35, max_incoming=2, max_outgoing=1)

    trees = extract(tc, 8)
    lst = []
    for i, t in enumerate(trees):
        vis = VisLineFormat(t, list(range(2000, 2017)))
        json_lst = vis.to_json_lst()
        lst.extend(json_lst)

    with open('/Users/ranxiao/Desktop/tropical_forest/visualization/lda_vis.json', 'w') as outfile:
        outfile.write(json.dumps(lst))






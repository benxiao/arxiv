import json
import re


# expression = re.compile(r'<entry>(.+?)</entry>', flags=re.DOTALL)
# summaries = set()
# for i in range(2000, 2017):
#     for j, x in enumerate(json.load(open('arxiv_dump_{}.json'.format(i)))):
#         for s in re.findall(expression, x[1]):
#             summaries.add(s)

print(len(json.load(open('arxiv_2000_2016.json'))))
#
# lst = json.load(open('arxiv_dump_2000.json'))
# for entry in re.findall(expression, lst[3][1]):
#     print(entry)
#     print('*'*100)
#
# print(len(summaries))


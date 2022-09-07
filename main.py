import jieba
file = open("D:\\AA_python\\党的十九大报告.txt", "r",encoding="utf-8")
txt = file.read()
file.close()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(20):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))

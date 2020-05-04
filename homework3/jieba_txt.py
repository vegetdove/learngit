# 7 对一篇中文文献, ;利用jieba库,
# 进行词频统计分析找出文章的关键词
# (取词频最高的前10个词语,作为文章的关键字);

import jieba

path = "D://CodeProjects/PythonProjects/homework3/viterbi.txt"

txt = open(path, "r", encoding='utf-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    
        # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    
# 根据词语出现的次数进行从大到小排序

print("文章的关键字为：\n")

for i in range(10):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
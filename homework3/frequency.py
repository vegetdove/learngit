# 6.对一篇英文小说，进行词频统计，输出前20个出现频率最高的单词；

path = "D://CodeProjects/PythonProjects/homework3/The old man and the sea.txt"

def getText() :
    txt = open(path,"r",encoding='gbk', errors='ignore').read()
    txt = txt.lower()
    for ch in '~!@#$%^&*\(\)_+`-={|}:"<>?[\\];,./\' ':
        txt = txt.replace(ch," ")
    return txt

sentence = getText()
result = {word:sentence.split().count(word) for word in set (sentence.split())}
result1 = sorted(result,key = lambda k : result[k])
result1.reverse()
i = 0
for j in result1 :
    if(i<20) :
        print(j,result[j])
        i += 1
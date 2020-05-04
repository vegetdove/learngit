#8 在2个文件中存放了英文计算机技术文章
# (可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 
# 请读取文章内容,进行词频的统计;
# 并分别输出统计结果到另外的文件存放;
# 比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,
# 相似度就是50%;重复了6个,相似度就是60% ,......);

path0 = "D://CodeProjects/PythonProjects/homework3/essay0.txt"
path1 = "D://CodeProjects/PythonProjects/homework3/essay1.txt"
path2 = "D://CodeProjects/PythonProjects/homework3/res0.txt"
path3 = "D://CodeProjects/PythonProjects/homework3/res1.txt"

def getText0() :
    txt = open(path0,"r",encoding='gbk', errors='ignore').read()
    txt = txt.lower()
    for ch in '~!@#$%^&*\(\)_+`-={|}:"<>?[\\];,./\' ':
        txt = txt.replace(ch," ")
    return txt

def getText1() :
    txt = open(path1,"r",encoding='gbk', errors='ignore').read()
    txt = txt.lower()
    for ch in '~!@#$%^&*\(\)_+`-={|}:"<>?[\\];,./\' ':
        txt = txt.replace(ch," ")
    return txt

sentence = getText0()
result = {word:sentence.split().count(word) for word in set (sentence.split())}
result1 = sorted(result,key = lambda k : result[k])
result1.reverse()
i = 0
with open(path2,"w") as f :
    for j in result1 :
        if(i<10) :
            f.write("%s %s"%(j,result[j]))
            f.write("\n")
            i += 1

sentence = getText1()
result = {word:sentence.split().count(word) for word in set (sentence.split())}
result1 = sorted(result,key = lambda k : result[k])
result1.reverse()
i = 0
with open(path3,"w") as f :
    for j in result1 :
        if(i<10) :
            f.write("%s %s"%(j,result[j]))
            f.write("\n")
            i += 1

word0 = []
word1 = []

with open(path2,"r") as f :
    for line in f.readlines() :
        word0.append(line.split()[0])

with open(path3,"r") as f :
    for line in f.readlines() :
        word1.append(line.split()[0])

countt = 0
for i in word0 :
    for j in word1 :
        if (i==j) :
            countt += 1

print(f"2篇文章相似度为 {countt*10}%")
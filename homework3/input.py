# 1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
# 将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；

print("请输入文件内容")

s = [];
for line in iter(input, ''):
    s.append(line.replace(',',''))

f = open("E:vegetdove/superintendent/learngit/homework3/input.txt","w")
for i in s :
    f.write(str(i))
    f.write("\n")

print("写入成功")
f.close()
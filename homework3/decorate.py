# 5 文件编程小项目
# 请完成以下文件综合编程迷你项目（可以利用list的insert函数）
# （1）创建一个Blowing in the wind.txt，其内容为...
# （2）在文件头部插入歌名“Blowin' in the wind”
# （3）在歌名后插入歌手名“Bob Dylan”
# （4）在文件末尾加上字符串“1962 by Warner Bros.Inc.”
# （5）在屏幕上打印文件内容

path = "D://CodeProjects/PythonProjects/homework3/song.txt"

with open(path,"w") as f :
    f.write("""
    How many roads must a man walk down
    Before they call him a man
    How many seas must a white dove sail
    Before she sleeps in the sand
    How many times must the cannon balls fly
    Before they're forever banned
    The answer my friend is blowing in the wind
    The answer is blowing in the wind 
    """)

with open(path,"r+") as f :
    old = f.read()
    f.seek(0)
    f.write("Blowin' in the wind                       ")
    f.write(old)

with open(path,"r+") as f :
    old = f.read()
    f.seek(25,0)
    f.write("Bob Dylan")

with open(path,"a+") as f :
    old = f.read()
    f.seek(0)
    f.write(old)
    f.write("   1962 by Warner Bros.Inc.")

with open(path,"r") as f :
    song = f.read()
    print(song)

import os

#练习1:pathlearn
def exer1() :
    pwd = os.path.abspath(".")
    print( os.path.abspath(pwd + r"\a"))
    print( os.path.basename(pwd + r'\a\a.txt') )   # 返回文件名
    print( os.path.dirname(pwd + r'\a\a.txt') )    # 返回目录路径
    print( os.path.split(pwd + r'\a\a.txt') )      # 分割文件名与路径
    print( os.path.join(pwd + r'\a','a.txt') )     # 将目录和文件名合成一个路径

#练习2:open
def exer2() :
    FileList = ["E:\\pylearn\\test1.txt",
                "E:\\test2.txt",
                "E:\\pylearn\\a_file\\test3.txt"]
    with open(FileList[0],"w") as file :
        file.write("hello")
    with open(FileList[1],"w") as file :
        file.write("hello")
    with open(FileList[2],"w") as file :
        file.write("hello")
    for i in FileList :
        os.remove(i)

#练习3:read0
def exer3() :
    with open(r"E:pylearn\a_file\a.py","r",encoding='UTF-8') as f :
        print(f.read())

#练习4、5:read&reorder
def exer45() :
    lines = []
    with open(r"E:pylearn\a_file\a.txt","r",encoding='UTF-8') as f:
        for perline in f.readlines():
            #print(perline)
            lines.append(perline.split())
    lines[1:] = sorted(lines[1:],key = lambda line:line[2])
    for perline in lines: #直接输出
            s = '{}{}{}'.format(perline[0], perline[1].center(13, ' '), perline[2])
            print(s)
    # with open(r"E:pylearn\a_file\b.txt","w",encoding='UTF-8') as f: #输出到文件
    #     for perline in lines:
    #         s = '{}{}{}'.format(perline[0], perline[1].center(13, ' '), perline[2])
    #         print(s)
    #         f.write(s + '\n')
    f.close()

if __name__ == "__main__":
    #exer1()
    #exer2()
    #exer3()
    exer45()
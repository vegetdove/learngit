# 6. 用面向对象，实现一个学生Python成绩管理系统
# 学生的信息存储在文件中
# 学生信息的字段有(班级、学号、姓名、Python成绩)
# 实现对学生信息及成绩的增、删、改、查方法

from student import Student
import os


class InfoMS:
    def __init__(self, filename, encoding='utf-8'):
        self._encoding = encoding
        self._filename = filename
        self._infos = []
        self.__load()

    def __load(self):
        if not os.path.isfile(self.filename):
            return

        with open(self.filename, 'r', encoding=self._encoding) as f:
            for line in f:
                info = line.split()
                s = Student(info[0], info[1], info[2], int(info[3]))
                self._infos.append(s)

    @property
    def filename(self):
        return self._filename

    @property
    def encoding(self):
        return self._encoding

    def add(self, no, clz, name, score):
        i = self.findIndex(no)
        if i != -1:
            print('学号重复，添加失败')
        else:
            self._infos.append(Student(no, clz, name, score))

    def delete(self, no):
        i = self.findIndex(no)
        if i == -1:
            print('指定学号的学生不存在 no: %s' % no)
        else:
            del self._infos[i]

    def update(self, no, clz, name, score):
        i = self.findIndex(no)
        if i == -1:
            print('指定学号的学生不存在 no: %s' % no)
        else:
            self._infos[i].clz = clz
            self._infos[i].name = name
            self._infos[i].score = score

    def find(self, no):
        i = self.findIndex(no)
        if i == -1:
            return None

        return self._infos[i]

    def findIndex(self, no):
        for i in range(len(self._infos)):
            if self._infos[i].no == no:
                break
        else:
            return -1

        return i

    def flush(self):
        with open(self.filename, 'w', encoding=self._encoding) as f:
            for s in self._infos:
                s.writeToFile(f)

    def printInfos(self):
        print('学号 班级 姓名 成绩')
        print('-' * 40)
        for s in self._infos:
            print('%-3s %s %s %3s' % (s.no, s.clz, s.name, s.score))

if __name__ == '__main__':
    os.chdir('E:/vegetdove/superintendent/learngit/homework6/StudentManage')
    i = InfoMS('stu.txt')

    i.add('001', '1801', 'Bob', 80)
    i.add('002', '1802', 'Alice', 78)
    i.add('003', '1803', 'Cindy', 99)
    i.printInfos()

    print()
    i.update('002', '1802', 'Alice', 90)
    i.delete('001')
    i.printInfos()

    i.flush()
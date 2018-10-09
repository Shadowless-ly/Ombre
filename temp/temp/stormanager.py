#!/usr/bin/env python
"""文件仓库版本管理工具

用于Option版本库的文件夹/文件管理工具，用于便捷的控制Option repo版本变更。
功能如下：
1.  为repo生成文件列表，记录文件位置，修改时间，以及md5值。
2.  可对比两份文件列表，获得变更文件列表。
3.  可依据历史文件列表获取当前文件夹的变更列表。
4.  通过变更列表生成补丁包(新增文件，控制脚本)
5.  回退补丁更新

"""


import os
import sys
import hashlib

echo = print

class File():
    """文件对象，Option仓库中的文件对象，拥有名称，路径，大小，修改时间，md5属性
    两文件可以直接使用运算符"==", "!="比较是否是相同文件
    """
    def __init__(self, fullname, size=10240):
        # fullname参数为文件绝对路径， size为计算md5值时单次读取文件字节数
        self.fullname = fullname
        self.parsefile()
        self.getmd5(size)

    def parsefile(self):
        # 解析文件完整路径，不存在则esixt属性为False,若存在则解析出目录名，文件名
        if os.path.exists(self.fullname):
            echo("[File][__init__]: This is no such file: %s" % self.fullname)
            self.exist = False
            self.dirname = None
            self.dirname = None
            self.size = None
            self.mtime = None
        else:
            self.exist = True
            self.dirname = os.path.dirname(self.fullname)
            self.basename = os.path.basename(self.fullname)
            self.size = os.path.getsize(self.fullname)
            self.mtime = os.path.getmtime(self.fullname)

    def getmd5(self, size):
        # 若文件存在计算其MD5值，size参数指定单次读取文件字节数
        md5 = hashlib.new("md5")
        if self.exist:
            with open(self.fullname, "rb") as f:
                while True:
                    data = f.read(size)
                    if data:
                        md5.update(data)
                    else:
                        break
            self.md5 = str.lower(md5.hexdigest())
        else:
            self.md5 = None
    
    def __eq__(self, other):
        try:
            return self.md5 == getattr(object, "md5", 0)
        except AttributeError:
            return False
    
    def __ne__(self, other):
        try:
            return self.md5 != getattr(object, "md5", 0)
        except AttributeError:
            return False


class FileManager():
    """管理指定目录所有文件对象，可生成filelist
    """
    def __init__(self, targetdir):
        # 遍历目标目录及其子目录所有文件，获取文件fullname列表
        self.filelist = []
        if os.path.exists(targetdir):
            echo("[FileManager][__init__]: Scanning target directory...")
            self.fullnamelist = [parentdir+os.sep+f for parentdir, _, files in os.walk(targetdir) for f in files]
        else:
            echo("[FileManager][__init__]: There is no such directory: %s" %targetdir)
            self.fullnamelist = []

    def init(self):
        if not self.fullnamelist:
            echo("[FileManager][init]: fullnamelist is empty!")
        else:
            echo("[FileManager][init]: update filelist...!")
            self.filelist = [File(f) for f in self.fullnamelist]
    
    def genfilelist(self, filename):
        if not self.filelist:
            echo("[FileManager][genfilelist]: filelist is empty, please init first!")
        else:
            with open(filename, "w") as f:
                for fobj in self.filelist:
                    f.writelines(fobj.fullname+";;"+fobj.md5+";;"+fobj.mtime)
        
if __name__ == "__main__":
    pass
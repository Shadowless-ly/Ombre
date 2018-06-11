import fileinput

for line in fileinput.input():
    meta = ["文件名:" + str(fileinput.filename()),
    " 文件描述符:" + str(fileinput.fileno()),
    " 行号:" + str(fileinput.filelineno()),
    " 首行:" + str(fileinput.isfirstline()),
    " 标准输入:" + str(fileinput.isstdin()) + " "]
    meta_ljust = [i.ljust(9) for i in meta]
    print(*meta_ljust, end="")
    print(line, end="")

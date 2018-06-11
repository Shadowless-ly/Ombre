import fileinput

for line in fileinput.input(openhook=fileinput.hook_encoded(encoding="gbk")):
    print(line, end="")
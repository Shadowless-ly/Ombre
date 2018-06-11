import fileinput

for line in fileinput.input(openhook=fileinput.hook_compressed):
    print(line.decode('utf-8'), end="")

import sys

def get_upper_list():
    content_list =  sys.stdin.readlines()
    return [i.upper() for i in content_list]

for line in get_upper_list():
    sys.stdout.write(line)

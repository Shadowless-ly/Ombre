import sys
str_raw = "55 49 53 2d 52 41 49 44 2d 31 30 30 30 2d 4d 32"
print(''.join([chr(int(i, 16)) for i in ["0x" + i for i in ((sys.argv[1:]) or str_raw.split())]]))
a = input("aaaa:")

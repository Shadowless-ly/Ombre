class DecToBin(object):
    def Convert(self, num):
        return bin(int(num))

if __name__ == "__main__":
    print(DecToBin().Convert(-8).replace('0b', ''))
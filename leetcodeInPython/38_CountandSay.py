import time
class Solution:
    
    def __init__(self):
        self.buffer_list = []
        self.buffer(5, ['1', '11', '21', '1211', '111221'])
        self.counter = self.countGen()

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 2 :
            return '1'
        if n > self.max_n:
            i = self.max_n
            temp_list = []
            while i < n:
                i += 1
                temp_list.append(next(self.counter))
            self.buffer(n, temp_list)
            return self.buffer_list[n-1]
        else:
            return self.buffer_list[n-1]

    def buffer(self, n, buffer_list):
        self.max_n = n
        self.buffer_list.extend(buffer_list)
    
    def countGen(self):
        say = sequence = '111221'
        while True:
            print('start countGen!')
            seek = 0
            count = 1
            sequence = say
            say = ''
            while seek < len(sequence):
                if seek + 1 <= len(sequence) - 1 and sequence[seek] == sequence[seek + 1]:
                    count += 1
                else:
                    say = say + str(count) + str(sequence[seek])
                    count = 1
                seek += 1
            yield say
begin_time = time.time()

sol = Solution()
print(sol.countAndSay(10))
print(sol.countAndSay(9))
print(sol.countAndSay(8))
print(sol.countAndSay(7))
print(sol.countAndSay(6))
print(sol.countAndSay(5))
print(sol.countAndSay(4))
print(sol.countAndSay(3))
print(sol.countAndSay(2))
print(sol.countAndSay(1))

# print(sol.countAndSay(1))
# print(sol.countAndSay(2))
# print(sol.countAndSay(3))
# print(sol.countAndSay(4))
# print(sol.countAndSay(5))
# print(sol.countAndSay(6))
# print(sol.countAndSay(7))
# print(sol.countAndSay(8))
# print(sol.countAndSay(9))
# print(sol.countAndSay(10))

end_time = time.time()
print('use %.15f seconds...' %(end_time-begin_time))
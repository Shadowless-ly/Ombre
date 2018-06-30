from collections import Counter

c = Counter('abcab')
print(c)
c['a'] += 1
print(c)

print(list(c.elements()))
print(c.items())
print(c.most_common())
c.subtract('aaa')
print(c)
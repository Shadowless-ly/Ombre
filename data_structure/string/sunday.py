#!/usr/bin/env python
#-*-coding:utf-8-*-

def sunday(string, substring):
	# i作为string的索引
    i = 0
    # j作为substring的索引
    j = 0
    # k作为查找目标字符在substring中的倒序索引
    k = 0
    # 准出条件len(string)-(i+1)到了不足以匹配len(substring)-(k+1)的长度
    while len(string)-(i+1) >= k+1 and j<=len(substring)-1:
        # 如果两字符不相同
        if string[i] != substring[j]:
            i = i + len(substring)-(j+1) + 1
            for s in range(len(substring)):
                print('i:', i, 'j', j, 's', s)
                if substring[len(substring)-s-1] == string[i]:
                    print('get it')
                    k = s
                    i = i - (len(substring)-k-1)
                    j = 0
                    break
        # 如果出现相同,继续向后匹配
        else:
            print('匹配string的第%s,值为%s' %(i, string[i]))
            print('匹配substring的第%s,值为%s' %(j, substring[j]))
            i += 1
            j += 1
            continue

    if j == len(substring):
        return i-j
    else:
        return None

def main():
    print(sunday('hello world, my name is liyang', 'li'))

if __name__ == '__main__':
    main()
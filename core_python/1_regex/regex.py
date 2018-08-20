"""Python re模块与正则表达式学习笔记

参考文档[python | 史上最全的正则表达式](https://blog.csdn.net/weixin_40907382/article/details/79654372)
1. Python re模块的使用，各个方法的不同与使用场景
2. 正则表达式语法
"""

import re
import datetime

########################
# re模块
########################

"""re模块的使用

1. re.findall(pattern, string, flags=0)
在字符串中查找负责规则的字符串，parttern为规则，string为目标字符串，flags为规则选项
返回结果为一个列表，存放这所有符合规则的字符串
若没有符合规则的字符串，返回一个空列表

>>> demo_string = '许多程序设计语言都支持利用正则表达式进行字符串操作。\
例如，在Perl中就内建了一个功能强大的正则表达式引擎。\
正则表达式这个概念最初是由Unix中的工具软件（例如sed和grep）普及开的。\
正则表达式通常缩写成“regex”，单数有regexp、regex，复数有regexps、regexes、regexen。'

>>> re.findall(r're\w+', demo_string)
['rep', 'regex', 'regexp', 'regex', 'regexps', 'regexes', 'regexen']

>>> re.findall("abc", demo_string)
[]


2. re.match(pattern, string, flags=0)
match为从字符串string开头开始匹配，如果开头没有匹配成功即失败。
match会返回一个MatchObject对象，其与组的划分至关重要。
如果匹配不成功，返回NoneType

>>> re.match('\w{3}', demo_string)
<_sre.SRE_Match object; span=(0, 3), match='许多程'>

>>> print(re.match('abc', demo_string))
None


3. re.search(pattern, string, flags=0)
search与match不同之处在于，当开头位置匹配不同，会跳过开头，继续向后寻找是否有匹配的字符串

>>> re.search('re\w+', demo_string)
<_sre.SRE_Match object; span=(85, 88), match='rep'>


4. match与search的其他特点：
注:re.match与re.search功能(参数)上对比re.compile过的Pattern对象是不够强大的。
match与search的分组group：
match与search匹配成功后会返回一个MatchObject对象，而失败为NoneType。注意判断匹配是否成功。

>>> s = 'Tom:9527 , Sharry:0003'
>>> m = re.match(r'(?P<name>\w+):(?P<num>\d+)', s)
>>> if m:
...     print(m.group())
Tom:9527

>>> m.group('name')
'Tom'

>>> m.group('num')
'9527'


5. re.finditer(pattern, string, flags=0)
finditer类似与findall和search的结合增强，返回一个迭代器。
每次返回值是一个匹配到的MatchObject。

>>> for i in re.finditer('re\w+', demo_string):
...     print(i.group(), i.span())
rep (85, 88)
regex (105, 110)
regexp (115, 121)
regex (122, 127)
regexps (131, 138)
regexes (139, 146)
regexen (147, 154)


6. re.sub(pattern, repl, string, count=0, flags=0)
字符串的替换和修改，re.sub比字符串对象提供的方法更强大一些。
在目标字符串中按照规则匹配字符串，再把他们替换成指定的字符串，可以设置次数。默认全部。
pattern时正则表达式，repl为用来替换的字符串，第三个参数为目标字符串，count为次数。

还有一个类似的函数re.subn(pattern, repl, string, count=0, flags=0)
两者参数一致，后者返回结果为一个元组，第一个元素为替换后的字符串，第二个元素为替换次数。

>>> s = 'I have a dog , you have a dog , he have a dog '
>>> re.sub(r'dog', 'cat', s)
'I have a cat , you have a cat , he have a cat '

>>> re.sub(r'dog', 'cat', s, count=2)
'I have a cat , you have a cat , he have a dog '

>>> re.subn(r'dog', 'cat', s)
('I have a cat , you have a cat , he have a cat ', 3)


7. re.split(pattern, string, maxsplit=0, flags=0)
切片函数，使用指定的规则在目标字符串中查找匹配的字符串，用以作为分解将字符串切割
与str.split方法类似，返回一个列表。
>>> s = 'I have a dog   ,   you have a dog  ,  he have a dog'
>>> re.split('\s*,\s*', s)
['I have a dog', 'you have a dog', 'he have a dog']


8. re.escape(pattern)
当执行正则匹配时，要匹配类似+*.这些符号，我们可以使用该函数进行转义。
>>> re.escape('.*?')
'\\.\\*\\?'


9. re的组和MatchObject
9.1 编译后的Pattern对象
我们可以将一个正则表达式使用re.compile函数编译后使用，这样不仅可以提升匹配速度，
还可以使用一些附加功能。
编译后生成一个Pattern对象，这个对象里面有很多方法，如findall,match,search,
finditer,sub,subn,split。只不过参数有所不同。
参数去除了pattern与flags，增加了pos与endpos用来表示查找区间。
Pattern还提供了一些方法查询其flags，pattern与groupindex
>>> p = re.compile( r'(?P<word>/b[a-z]+/b)|(?P<num>/b/d+/b)|(?P<id>/b[a-z_]+/w*/b)', re.I)
>>> p.flags
34
>>> p.pattern
'(?P<word>/b[a-z]+/b)|(?P<num>/b/d+/b)|(?P<id>/b[a-z_]+/w*/b)'
>>> p.groupindex
mappingproxy({'word': 1, 'num': 2, 'id': 3})

9.2 组与MatchObject
正则表达式中每个组都有一个序号，从1开始，0为本身。
>>> p = re.compile( r'(?P<name>[a-z]+)/s+(?P<age>/d+)/s+(?P<tel>/d+).*', re.I )
>>> p.groupindex
mappingproxy({'name': 1, 'age': 2, 'tel': 3})
>>> s = 'Tom 24 88888888 <='
>>> m = p.search(s)
>>> m.groups()
('Tom', '24', '88888888')
>>> m.group('name')
'Tom'
>>> m.group(1)
'Tom'
>>> m.group(0)
'Tom 24 88888888 <='
>>> m.group()
'Tom 24 88888888 <='

MatchObject对象
group([index[id]]) 返回匹配的组，默认为group(0)，即全部正则值
groups() 返回全部的组
groupdict() 返回以组名为key，匹配内容为values的字典

start([group]) 返回开始匹配的位置
end([group]) 返回结束位置
span([group]) 返回(开始，结束)位置
pos 搜索开始位置
endpos 搜索结束位置
lastindex 最后匹配的组的序号
lastgroup 最后匹配的组名
re 创建这个MatchObject对象的表达式
string 匹配的目标字符串

expand功能：
expand(template)根据一个模板，用找到的内容替换模板里相应的位置
可以使用\g<index|name>或\index来指代一个组
>>> m.expand(r'name is \g<1>, age is \g<age>, tel is \3')
'name is Tom, age is 24, tel is 88888888'


附：
flags
标识指定多个，使用|运算连接

I   IGNORECASE忽略大小写

L   LOCAL字符集本地化字符集本地化。
    这个功能是为了支持多语言版本的字符集使用环境的，
    比如在转义符/w ，在英文环境下，它代表[a-zA-Z0-9]，
    即所以英文字符和数字。如果在一个法语环境下使用，
    缺省设置下，不能匹配 "é" 或 "ç" 。
    加上这 L 选项和就可以匹配了。
    不过这个对于中文环境似乎没有什么用，
    它仍然不能匹配中文字符。

M   MULTILINE多行匹配多行匹配。
    在这个模式下 ’^’( 代表字符串开头 ) 和 ’$’( 代表字符串结尾 )
    将能够匹配多行的情况，成为行首和行尾标记。
>>> s='123 456/n789 012/n345 678'
>>> rc=re.compile(r'^/d+')
['123']
>>> rcm=re.compile(r'^/d+',re.M)
['123', '789', '345']

S   DOTALL'.'号可以匹配所有字符，使用该标记，'.'也可以匹配到'\n'了。

U   UNICODE \w \W \b \B \d \D \s \S将使用Unicode

X   VERBOSE这个选项将忽略表达式中的空白，且支持#来写注释。
>>> rc = re.compile(
r"
/d+|[a-zA-Z]+
")
#匹配一个数字或者单词
>>> rc = re.compile(r"
# start a rule
/d+ # number| [a-zA-Z]+ # word", re.VERBOSE)
该模式如果要匹配空格，需要\ 转义
"""


#######################
# 正则表达式规范
#######################

"""正则表达式规范
模式    描述
^       字符串开头
$       字符串结尾
.       任意字符，除换行符，可以re.DOTALL,re.S匹配所有字符
[...]   一组字符[amk]代表匹配'a','m'或'k'
[^...]  不在[]中的字符会被匹配到
re*     0个或多个
re+     1个或多个
re{n}   n个
re{n,}  n个或多个
re{n,m} n个到m个
a|b     a或者b
(re)    G匹配括号内的表达式，也表示一个组
(?imx)  正则表达式使用I,M,X标记,作用于全部正则
(?-imx:re) 正则表达式关闭I,M,X标记，作用于括号内
(?:re)  类似与(...)但不是一个组
(?imx:re)   在括号内使用I,M,X标记
(?#...) 注释
(?=re)  后向界定，你希望匹配的字符串后面应该出现的字符串。可以是正则。
(?!re)  后向否定界定符
(?<=re) 前向肯定界定符,你希望匹配的字符串前面应该出现的字符串，不能是正则，必须为正常字符串。
(?<!re) 前向否定界定符。不能是正则，必须为正常字符串。
(?>re)  独立的匹配模式，省去回溯
\w      匹配字母，数字
\W      匹配非字母，数字
\s      匹配空白符\t\n\r\f
\S      匹配非空字符
\d      匹配数字[0-9]
\D      匹配非数字
\A      匹配字符串开始
\z      匹配字符串结束
\Z      匹配字符串结束，如果存在换行，只匹配到换行前的结束字符
\g      获取匹配到组的结果\g<index|name> \index
\G      匹配最后匹配完成的位置
\b      匹配一个单词的边界，单词和空格之间，'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
\B      非单词边界，'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
\n      换行符
\t      制表符
\1...\9 第n个分组 \g<index|name>
\10     第10个分组，如果未经匹配，则为8进制字符码的表达式


1. ()  无命名组
最基本的组是由一对圆括号括起来的正则式。
>>> s = ‘aaa111aaa , bbb222 , 333ccc ‘
>>> re.findall (r'[a-z]+(/d+)[a-z]+' , s )
['111']

可以看到 findall 函数只返回了包含在 ’()’ 中的内容，
而虽然前面和后面的内容都匹配成功了，却并不包含在结果中。

2. (?P<name>)命名组
为该组取一个名字，后续可以调用它

3. (?P=name)在正则表达式中调用已匹配的命名组
也可直接使用\index

4. (?(id/name)yes-pattern|no-pattern) 判断指定组是否已匹配，执行相应的规则
这个规则的含义是，如果 id/name 指定的组在前面匹配成功了，
则执行 yes-pattern 的正则式，否则执行 no-pattern 的正则式。
(<)?/s*(/w+@/w+)/s*(?(1)>)
'<usr1@mail1>  usr2@maill2 <usr3@mail3   usr4@mail4>  < usr5@mail5 '
[('<', 'usr1@mail1'), ('', 'usr2@maill2'), ('', 'usr3@mail3'), ('', 'usr4@mail4'), ('', 'usr5@mail5')]
"""


# # 识别后续字符串
# str_lst = ["bat", "bit", "but", "hat", "hit", "hut"]
# macth_word = re.compile("[bh][aiu]t", re.IGNORECASE)
# for i in str_lst:
#     if macth_word.match(i): print(macth_word.match(i).group())


date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
date = "当前时间：" + date
print(date)
print(re.sub(r"(?i).*?(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+).*", r"\g<year>,\g<month>,\g<day>", date))
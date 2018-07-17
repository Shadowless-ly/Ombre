def step():
    a = 0
    while True:
        if a == -1:
            return
        print(a)
        a = yield a

"""
使用yield from改进生成器
yield from语法
1.  让嵌套生成器不必通过循环迭代yield，而是直接yield from
2.  在子生成器与原生成器的调用者之间打开双向通道，两者可以直接通信
"""

############################################################
# 让嵌套生成器不必通过循环迭代yield，而是直接yield from
############################################################
def gen_one():
    subgen = range(10)
    yield from subgen

def gen_two():
    subgen = range(10)
    for item in subgen:
        yield item

############################################################
# 在子生成器与原生成器的调用者之间打开双向通道，两者可以直接通信
############################################################
def gen():
    yield from subgen()

def subgen():
    while True:
        x = yield
        yield x + 1

def main():
    g = gen()
    next(g)     # 驱动生成器g开始执行到第一个yield
    retval = g.send(1)      # 看似向生成器gen()发送数据
    print(retval)       # 返回2
    g.throw(StopIteration)      # 看似向gen()抛入异常
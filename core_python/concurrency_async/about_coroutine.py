"""
# 协程

* 协程(Co-routine),即是协作式的例程。
是非抢占式的多任务子例程的概括，可与允许有多个入口点在例程中确定的位置来控制程序的暂停与恢复执行。

## 基于生成器的协程

生成器(Generator)和协程的特点很像，每一次迭代之间会暂停执行，继续下一次迭代的时候不会丢失先前的状态。
为了支持生成器做简单的协程，Python2.5对生成器进行了增强(PEP 342)
生成器可以使用yield暂停执行和向外返回数据
也可以通过send()向生成器内发送数据
还可以通过throw()向生成器内抛出异常

"""

"""
### 未来对象(Future)

不使用回调的方式，如何获知异步调用的结果？可以先设计一个对象，异步调用完成后就把结果放入其中，这种对象叫做Future对象。
未来对象有一个result属性，用于存放未来的执行结果。还有一个set_result()方法，用以设置result，并且会在给定result后运行事先给
future添加的回调。回调通过add_done_callback()方法添加。
此处回调使用不同于之前回调。
"""

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import asyncio

selectors = DefaultSelector()
stopped= False
urls_todo = ['www.163.com']

class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        print('add call back')
        self._callbacks.append(fn)

    def set_result(self, result):
        print('set result')
        self.result = result
        for fn in self._callbacks:
            fn(self)

class Crawler:
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        # 设置socket为非阻塞
        sock.setblocking(False)
        try:
            # 非阻塞方式创建连接
            sock.connect((url, 80))
        except BlockingIOError:
            pass
        # 创建Future对象
        f = Future()
        # 注册回调函数，当返回连接，设置执行结果为None
        def on_connected():
            # 设置future的result为None
            # set_result会调用其内部注册的回调函数
            f.set_result(None)
        selectors.register(sock.fileno(), EVENT_WRITE, on_connected)
        # 交出执行权，返回Future对象
        yield f
        # 获得执行权，取消注册
        selectors.unregister(sock.fileno())
        get = 'GET {0} HTTP/1.0\r\nHost: www.163.com\r\n\r\n'.format(self.url)
        # 将数据发送到内核缓冲区
        sock.send(get.encode('utf-8'))
        # 声明全局变量stopped状态，用于确认是否完成全部任务
        global stopped

        while True:
            f = Future()

            def on_readable():
                f.set_result(sock.recv(4096))

            selectors.register(sock.fileno(), EVENT_READ, on_readable)
            chunk = yield f
            selectors.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                urls_todo.remove(self.url)
                if not urls_todo:
                    stopped = True
                break

class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coro.send(future.result)
        except StopAsyncIteration:
            return
        next_future.add_done_callback(self.step)
        print(next_future._callbacks)
                 
"""
上述代码中，Task封装了coro对象，即初始化传递给他的对象，被管理的任务是待执行的协程
这里的coro就是fetch()生成器，还有一个step方法，在初始化的时候就会执行一遍，step()内
会调用生成器的send()方法，初始化第一次发送的是None就驱动了core即fetch()的第一次执行。
"""

def loop():
    while not stopped:
        events = selectors.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

"""
整体流程：
1. 在要执行异步IO时创建Furture对象。
2. 监控sock.fb的可读写状态，注册selector回调（将结果保存于Future对象的result中）。
3. yield Future对象。
3. 在step中取得Future对象，注册设置Future set_result时的回调函数。
4. 事件循环，直到sock.fb状态满足。
5. 触发selector回调，设置Future的result值。
6. 设置值后触发Future回调，进入Step，将Future的值send到协程，继续运行协程，直到再次yield
"""
if __name__ == "__main__":
    for url in urls_todo:
        crawler = Crawler(url)
        Task(crawler.fetch())
    loop()

"""
重构代码
抽象socket连接功能
"""
# def connect(sock, address):
#     f = Future()
#     sock.setblocking(False)
#     try:
#         sock.connect(address)
#     except BlockingIOError:
#         pass
    
#     def on_connected():
#         f.set_result(None)

#     selectors.register(sock.fileno(), EVENT_WRITE, on_connected)
#     yield from f
#     selectors.unregister(sock.fileno())

# def read(sock):
#     f = Future()

#     def on_readable():
#         f.set_result(sock.recv(4096))

#     selectors.register(sock.fileno(), EVENT_READ, on_readable)
#     chunk = yield from f
#     selectors.unregister(sock.fileno())
#     return chunk

# def read_all(sock):
#     response = []
#     chunk = yield from read(sock)
#     while chunk:
#         response.append(chunk)
#         chunk = yield from read(sock)
#     return b''.join(response)


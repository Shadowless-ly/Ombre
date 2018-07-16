"""
# 相关概念

## 进程(Process)

在面向进程设计的操作系统中(linux2.4及以前)，进程是程序运行的基本单位；而在面向线程设计的操作系统中(linux2.6以及之后)，进程只是线程的容器，操作系统调度的单位是线程。
进程只是用于隔离不同的进程，不同进程间资源不同享，进程内资源可以共享。
进程的基本模型和基本行为是由操作系统定义的，编程语言只能遵照实现。

### 子进程，父进程，主进程

可以从一个进程启动另一个进程，新启动的进程称为子进程，启动子进程的进程称为父进程，原始最先执行的进程称为主进程。

## 线程(Thread)

线程是现在操作系统调度任务的基本单位，是进程的组成部分，同一进程下的多个不同线程可以共享进程的计算机资源，各个进程之间的资源一般不共享。
操作系统使用线程模型，是为了提供将任务分解为多个子任务并发或并行运行的解决方案，提高程序的执行效率。

# 子线程，父线程，主线程

可以从一个线程启动别的线程，被启动的为子线程，原来的是父线程，原始最先执行的为主线程。

# 例程(Routine)

语言级别内定义可以被调动的代码段，为了完成某个特定功能而封装在一起的一系列指令。一般编程语言都用称为函数或方法的代发结构来体现。

## 子例程(Subroutine)

例程中定义的例程。注意例程可以嵌套定义，而且例程也本就是代码拆分设计的子程序。

# 并发(Concurrent)

并发描述的是程序的组织结构。指程序要被设计成多个可独立执行的子任务(以利用有限的计算机资源十多个任务可以被实时或者近实时执行为目的)

# 并行(parallel)

并行是指程序的执行状态。指多个任务同时在多个CPU上执行(以利用富余的计算机资源加速完成多个任务为目的)

# 协程(Co-routine)

Coroutine也就是corporate routine，翻译为协同的例程。此概念和进程与线程类似，也叫做轻量级进程。
* 协程是非抢占式的多任务子例程的概括，可以允许多个入口点在例程中确认的位置来控制程序的暂停和恢复执行 *
多个入口点可以在一个协程中多次使用如yield的关键字，每个yield的位置，都是程序员可以使之让出执行权、暂停、恢复、传递信号、注入执行结果等操作。
函数在线程中执行，自然协程是在线程中执行，多个协程共享该线程拥有的资源，由于协程就是函数或方法，在线程运行初始化时，所以，和函数一样，协程的数据结构存放在线程的栈内存中。
* 所以协程的切换，实际上就是函数的调用，是在线程的栈内存中完成的 *
进程和线程的切换，要保存很复杂的状态，内存占用也大，操作系统调度复杂，所以协程的切换开销很小。
协程也是可以跨线程调度的，如同一个函数可以放到另一个线程去执行一样。

1. 相同点：
    二者都是可以看做一种执行流，该执行流可以挂起，并且将来又可以在你挂起的地方恢复。
    当我们挂起一个执行流时我们需要保存一些东西：
        a. 栈，如果你不保存栈，那么局部变量无法恢复，函数调用链也无法恢复
        b. 寄存器状态，如EIP如果没有则恢复时无法得知执行哪一条指令，
        如ESP，EBP，如果不保存，即便是拥有完整的栈也不知道如何使用。
    这两个就是所谓的上下文，continuation，在执行流切换时，这两个东西必须保存，就如同内核调用进程一样。

2. 不同点：
    a. 执行流的调度者不同，进程是内核调度，而协程是在用户态调度。也就是说进程的上下文是在内核态保存回复的，而协程是在用户态保存恢复的，代价更低。
    b. 进程会被抢占，而协程不会，使用yield原语，一个进程调用yield则会让出CPU，其他进程就有机会执行。
    c. 对于内存的占用不同，实际上协程只需要4K的栈就够了，而内存占用的内存要大很多。
    d. 从操作系统来讲，多协程是单线程，单进程的。

异步框架:Tornado，Twisted，Gevent
而Flask，Django等传统WEB框架为非异步框架。
Python3增加了async库和async/await语法，可以简洁高效的使用Python异步。

# 什么是异步编程

## 阻塞

*   程序未取得计算资源时被挂起的状态
*   程序在等待某个操作完成期间，自身无法继续干别的事情，则称改程序在操作上是阻塞的
*   常见的阻塞形式：网络I/O、磁盘I/O、用户输入阻塞等

包括CPU在切换上下文时，所有进程都是无法真正干活的，也会被阻塞。

## 非阻塞

*   程序在等待过程中，自身不被阻塞，可以继续干别的事情，则称改程序在该操作上时非阻塞的。
*   非阻塞并不是在任何程序级别，任何情况下都存在的
*   仅当程序封装的级别可以囊括地理的子程序单元时，他才可能存在非阻塞状态。

非阻塞的存在是因为阻塞存在。

## 同步

*   不同程序单元为了完成某个任务，在执行过程中靠某种通信方式以协调一致，称这些程序单元是同步执行的。
*   例如购物系统中更新商品库存，需要用'行锁'作为通信信号，让不同请求强制排队按序执行，那更新库存的操作就是同步的。
*   同步意味着有序

## 异步

*   为了完成某个任务，不同程序单元之间无需通信协调，也能完成任务的方式
*   不相关的程序单元之间可以是异步的
*   异步意味着无序

* 通信方式 * 通常是指异步与并发编程提供的同步原语，如信号量，锁，同步队列等。

# 异步编程

*   以进程、线程、协程、函数/方法作为执行任务程序的基本单位，结合回调，事件循环，信号量等机制，以提高程序整体执行效率和并发能力的编程方式。

*   简化异步模型：一次只允许处理一个事件。如果某事件处理程序需要长时间执行，所有其他部分都会被阻塞。

*   * 一旦采取异步编程，每个异步调用必须足够小 *
"""

# 同步阻塞方式
# 使用socket连接到发送网络请求再到读取相应数据，顺序执行：

import socket
import time


def blocking_way():
    sock = socket.socket()
    # blocking
    sock.connect(('172.16.16.211', 80))
    request = 'GET / HTTP/1.0\r\nHost: 172.16.16.211\r\n\r\n'
    sock.send(request.encode('utf-8'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        # blocking
        chunk = sock.recv(4096)
    return response

# 单线程同步方式
def sync_way():
    res = []
    for i in range(100):
        res.append(blocking_way())
    return len(res)


# 多进程方式
from concurrent import futures


def process_way():
    workers = 10
    with futures.ProcessPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])

# 多线程方式

def thread_way():
    workers = 10
    with futures.ThreadPoolExecutor(workers) as executor:
        futs = {executor.submit(blocking_way) for i in range(10)}
    return len([fut.result() for fut in futs])


# 非阻塞方式

def noblocking_way():
    sock = socket.socket()
    # 设置在socket上的阻塞调用都改为非阻塞的方法
    sock.setblocking(False)
    try:
        sock.connect(('172.16.16.211', 80))
    except BlockingIOError:
        # 非阻塞连接过程中也会抛出异常
        pass
    request = 'GET / HTTP/1.0\r\nHost: 172.16.16.211\r\n\r\n'
    data = request.encode('utf-8')
    while True:
        try:
            sock.send(data)
            # 直到send不抛异常，则发送完成
            break
        except OSError:
            pass

    reponse = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                reponse += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return reponse


def async_way():
    res = []
    for i in range(100):
        res.append(noblocking_way())
    return len(res)


def main():
    start = time.time()
    # print(sync_way())
    # print(process_way())
    # print(thread_way())
    print(async_way())
    end = time.time()
    print('time:', end-start)

"""
# 非阻塞改进

## epool

判断非阻塞调用是否就绪如果OS能做，是不是应用程序就可以不用自己去等待和判断，可以利用这个空闲去做其他事情。
所以OS将I/O状态的变化封装成了事件通知，如可读事件，可写事件。而且提供了专门的系统模块让应用程序可以接收事件通知。
这个模块就是`select`，让应用程序可以通过`select`注册文件描述符和回调函数。当文件描述符状态发生变化时，select就调用回调函数。

由于select算法效率比较低，后来改进为poll，再后来BSD内核改进成kqueue模块，而linux内核改进成了epoll模块。这四个模块作用相同，
暴露的API也几乎一致，区别在于kqueue和epoll在处理大量文件描述符时效率更高。

## 回调(Callback)

把I/O事件的等待和监听任务都交给了OS，那OS在知道I/O状态发生改变后(例如socket连接已经建立成功可发送数据)，只能回调。
需要我们将发送数据与读取数据封装成独立的函数，让epoll代替应用程序监听socket状态。

"""

from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

selector = DefaultSelector()
stopped = False
urls_todo = {'/', '/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9'}

class Crawler:
    def __init__(self, url):
        self.url = url
        self.sock = None
        self.response = b''
    
    def fetch(self):
        self.sock = socket.socket()
        # 设置socket为非阻塞
        self.sock.setblocking(False)
        try:
            self.sock.connect(('172.16.16.211', 80))
        except BlockingIOError:
            pass
        # 注册回调函数，当连接建立，文件描述符可写，调用写方法
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)
    
    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = 'GET {0} http/1.0\r\nHost: 172.16.16.211\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('utf-8'))
        # 注册回调函数，当连接建立，文件描述符可读，调用读方法
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        global stopped
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            selector.unregister(key.fd)
            urls_todo.remove(self.url)
            if not urls_todo:
                stopped = True

"""
事件循环(Event Loop)
要抓取10个不同的页面，就需要10个实例，那么将会有20个事件等待发生。
我们可以写一个循环，去访问selector模块，等待它告诉我们当前是哪个事件发生了，对应哪个回调。
* 这个等待事件通知的循环，称之为事件循环 *
>>> def loop():
...     while not stopped:
...         events = selectors.select()
...         for event_key, event_mask in events:
...             callback = event_key.data
...             callback(event_key, event_mask)

上述代码中，使用stopped全局变量控制事件循环何时停止。当urls_todo消耗完毕后，会标记stopped为True。

`selectors.select()`是一个阻塞调用，如果事件不发生，那么应用没有事件可处理，就阻塞在此等待事件发生。
下面是创建10个下载任务，启动事件循环：
>>> if __name__ == '__main__':
...     import time
...     start = time.time()
...     for url in urls_todo:
...         crawler = Crawler(url)
...         crawler.fetch()
...     loop()
...     print(time.time() - start)

"""


if __name__ == '__main__':
    main()
    

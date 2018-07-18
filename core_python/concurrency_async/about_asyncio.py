"""
asyncio介绍
在Python3.4引入，提供了基于协程做异步I/O编写单线程并发代码的基础设施。
在Python3.6正式成为标准库，其核心组件包括事件循环(Event Loop),协程(Coroutine)
、任务(Task)、未来对象(Future)以及其他一些扩充和辅助性质的模块。
在引入asyncio时，提供了@asyncio.coroutine用于装饰使用了yield from的函数，
以标记其为协程，但是不强制使用这么装饰器。
但因为yield和yield from语法存在误导，在Python3.5中新增了async/await语法

"""

import asyncio
import aiohttp

host = 'http://www.163.com'
urls_todo = ['/', '/', '/', '/', '/', '/', '/']

loop = asyncio.get_event_loop()

async def fetch(url, name):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            response = await response.read()
            print(name)
            return response

if __name__ == '__main__':
    # print(list(zip(range(7),urls_todo)))
    import time
    start = time.time()
    tasks = [fetch(host + url, name) for name, url in zip(range(7),urls_todo)]
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time() - start)

"""
对比生成器版的协程，使用asyncio库后变化很大：

没有了yield 或 yield from，而是async/await
没有了自造的loop()，取而代之的是asyncio.get_event_loop()
无需自己在socket上做异步操作，不用显式地注册和注销事件，aiohttp库已经代劳
没有了显式的 Future 和 Task，asyncio已封装
更少量的代码，更优雅的设计
说明：我们这里发送和接收HTTP请求不再自己操作socket的原因是，在实际做业务项目的过程中，
要处理妥善地HTTP协议会很复杂，我们需要的是功能完善的异步HTTP客户端，业界已经有了成熟的解决方案，DRY不是吗？

和同步阻塞版的代码对比：
异步化
代码量相当（引入aiohttp框架后更少）
代码逻辑同样简单，跟同步代码一样的结构、一样的逻辑
接近10倍的性能提升


结语

到此为止，我们已经深入地学习了异步编程是什么、为什么、在Python里是怎么样发展的。
我们找到了一种让代码看起来跟同步代码一样简单，而效率却提升N倍（具体提升情况取决于项目规模、网络环境、实现细节）的异步编程方法。它也没有回调的那些缺点。

"""

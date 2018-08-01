import logging; logging.basicConfig(level=logging.INFO)
import asyncio
import os
import json
import time
from aiohttp import web
from functools import wraps

def get(path):
    """定义装饰器 @get('/path')
    为函数附加URL信息与GET请求方式
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

def post(path):
    """定义装饰器 @post('/path')
    为函数附加URL信息与POST请求方法
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

@get('/blog/{id}')
def get_blog(id):
    pass

@get('/api/comments')
def api_comments(*, page='1'):
    pass


class RequestHandler(object):
    """URL处理函数不一定是一个coroutine，因此我们可以使用RequestHandler()来封装一个URL处理函数
    RequestHandler是一个类，定义了__call__()方法，所以可以将其实例视为函数直接调用
    RequestHandler的目的时从URL函数中分析其需要接收的参数，从request中获取必要的参数
    调用URL函数然后把结果转换为web.Response对象，这样就完全符合aiohttp框架的要求
    """
    def __init__(self, app, fn):
        self._app = app
        self._func = fn

    async def __call__(self, request):
        pass

def index(request):
    return web.Response(body=b'<h1>Hello world!</h1>', content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server start at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
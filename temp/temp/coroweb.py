import logging; logging.basicConfig(level=logging.INFO)
import asyncio
import os
import json
import time
from aiohttp import web
from functools import wraps
import inspect
import functools


#############封装视图函数###########
# 建立视图函数装饰器，将请求处理函数
# 与URL路由，请求方式关联起来
##################################
def Handler_decorator(path, *, method):
    """定义装饰器 @get('/path')
    为函数附加URL信息与请求方式
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = method
        wrapper.__route__ = path
        return wrapper
    return decorator

# def post(path):
#     """定义装饰器 @post('/path')
#     为函数附加URL信息与POST请求方法
#     """
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kw):
#             return func(*args, **kw)
#         wrapper.__method__ = 'POST'
#         wrapper.__route__ = path
#         return wrapper
#     return decorator

# 使用装饰器，直接将一个函数映射成为视图函数
@get('/blog/{id}')
def get_blog(id):
    pass

@get('/api/comments')
def api_comments(*, page='1'):
    pass

get = functools.partial(Handler_decorator, method='get')
post = functools.partial(Handler_decorator, method='post')

############处理request对象########
# 视图函数需要request对象的信息才可以正确运行
# 我们需要从request对象提取视图函数所需参数
# 且并非所有视图函数都是coroutine
# 需要一个能够处理request请求的类对视图函数进行封装
##################################
"""使用inspect模块检查视图函数的参数

inspect.Parameter.kind 类型
POSITIONAL_ONLY 位置参数
KEYWORD_ONLY    命名关键字参数
VAR_POSITIONAL  可选参数 *args
VAR_KEYWORD 关键字参数 **kw
POSITIONAL_OR_KEYWORD   位置或必选参数
"""
def get_required_kw_args(fn):
    # 获取无默认值的命名关键字参数
    args = []
    params = inspect.signature(fn).parameters
    for name,param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)

def get_named_kw_args(fn):
    # 获取命名关键字参数
    '''
	def foo(a, b = 10, *c, d,**kw): pass
	sig = inspect.signature(foo) ==> <Signature (a, b=10, *c, d, **kw)>
	sig.parameters ==>  mappingproxy(OrderedDict([('a', <Parameter "a">), ...]))
	sig.parameters.items() ==> odict_items([('a', <Parameter "a">), ...)])
	sig.parameters.values() ==>  odict_values([<Parameter "a">, ...])
	sig.parameters.keys() ==>  odict_keys(['a', 'b', 'c', 'd', 'kw'])
    '''
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)

def has_named_kw_args(fn):
    # 判断是否有命名关键字参数
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True

def has_var_kw_args(fn):
    # 判断是否有关键字参数
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True

def has_request_arg(fn):
    # 判断是否有名为‘request’的参数，且在位置参数的最后
    params = inspect.signature(fn).parameters
    found = False
    for name, param in param.items():
        if name == 'request':
            found = True
        if found and (
            param.kind != inspect.Parameter.VAR_POSITIONAL and
            param.kind != inspect.Parameter.KEYWORD_ONLY and
            param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function:%s%s' % (fn.__name__, str(sig)))
    return found


############提取request中的参数########
# request是经过aiohttp包装后的对象，本质是http请求
# 由请求状态(status)、请求首部(header)、内容实体(body)组成
# 我们需要的参数包含在内容实体以及请求状态URI中
# request对象封装了HTTP请求，可以通过request的属性调取值
#####################################

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
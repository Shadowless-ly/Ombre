import logging

"""basicConfig参数;
filename: 指定日志文件名;
filemode: 和file函数意义相同，制定日志文件的打开模式，'w' or 'a';
format: 指定输出的格式和内容.
    %(levelno)s: 日志级别数值
    %(levelname)s:日志级别名称
    %(pathname)s:当前程序路径，sys.argv[0]
    %(filename)s:当前执行程序名
    %(funcName)s:日志的当前函数
    %(lineno)s:当前行号
    %(asctime)s:日志时间
    %(thread)d:线程ID
    %(threadName)s:线程名称
    %(process)d:进程ID
    %(message)s:日志信息
datafmp: 指定时间格式，同time.strftime();
level: 设置日志级别，默认logging.WARNNING;
stream: 指定将日志的输出流，可以sys.stderr,sys.stdout或文件，默认sys.stderr,当filename也指定，stream被忽略；
"""
logging.basicConfig()
# 基本使用

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# logger = logging.getLogger(__name__)

# 等级
# logger.debug("debug message")
# logger.info("start print log")
# logger.debug("Do somthing")
# logger.warning("Something maybe fail")
# logger.critical("something error")
# print(logging.DEBUG)
logging.getLogger

"""使用logging的handler,logger,与formatter
handler类型有以下几种：
StreamHandler: 日志输出到流，可以时sys.stderr或sys.stdout或文件
FileHandler: 日志输出到文件
BaseRotatingHandler: 基本的日志回滚方式
RotatingHandler: 日志回滚方式，支持日志文件最大数量和日志文件回滚
TimeRotatingHandler: 日志回滚方式，在一定时间区域回滚日志文件
SocketHandler: 远程输出到TCP/IP sockets
DatagramHandler: 远程输出日志到UDP socckets
SMTPHandler: 远程输出日志到邮件地址
SysLogHandler: 日志输出到syslog
NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志
MemoryHandler: 日志输出到内存中的指定buffer
HTTPHandler: 通过"get","post"远程输出到HTTP服务器
"""

# 将日志输出到文件与屏幕

# 设置logging，创建一个FileHandler，将其添加到logger，然后将日志写入到制定文件
# 新建一个日志记录器,名称为模块名
file_logger = logging.getLogger(__name__)
# 设置日志等级为INFO
file_logger.setLevel(level=logging.INFO)
# 新建一个日志处理器，指定日志文件为log.log
file_handler = logging.FileHandler("log.log")

# 新建日志流处理器
console_handler = logging.StreamHandler()
# 设置日志等级
console_handler.setLevel(logging.ERROR)


# 设置日志处理器的日志等级为INFO
file_handler.setLevel(level=logging.INFO)
# 新建日志格式化器，设置格式
formatter = logging.Formatter("%(pathname)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s")
# 设置日志处理器的格式化工具为目标格式化器
file_handler.setFormatter(formatter)

# 添加日志记录器的处理装置为目标日志处理器
file_logger.addHandler(file_handler)
# 添加日志记录器的处理装置为日志流处理器
file_logger.addHandler(console_handler)

# file_logger.info("start print log")
# file_logger.debug("Do somting")
# file_logger.warning("Something maybe fail.")
# file_logger.error("Something wrong!")



"""日志回滚
"""
from logging.handlers import RotatingFileHandler

rHandler = RotatingFileHandler("log/rotating.log", maxBytes=1*1024, backupCount=3)
rHandler.setLevel(logging.INFO)
rHandler.setFormatter(formatter)

file_logger.addHandler(rHandler)

file_logger.info("start print log")
file_logger.debug("Do somting")
file_logger.warning("Something maybe fail.")
file_logger.error("Something wrong!")

"""可以设置不同的日志等级，用于控制日志的输出，

日志等级：使用范围

FATAL：致命错误
CRITICAL：特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
ERROR：发生错误时，如IO操作失败或者连接问题
WARNING：发生很重要的事件，但是并不是错误时，如用户登录密码错误
INFO：处理请求或者状态变化等日常事务
DEBUG：调试过程中使用DEBUG等级，如算法中每个循环的中间状态
"""

"""捕获traceback
"""
try:
    open("sklearn.txt","rb")
except (SystemExit,KeyboardInterrupt):
    raise
except Exception:
    # file_logger.error("Faild to open sklearn.txt from logger.error",exc_info = True)
    file_logger.excpetion("Faild to open sklearn.txt from logger.error")


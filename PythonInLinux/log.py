import logging


# 基本使用

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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



# 等级
logger.debug("debug message")
logger.info("start print log")
logger.debug("Do somthing")
logger.warning("Something maybe fail")
logger.critical("something error")
print(logging.DEBUG)


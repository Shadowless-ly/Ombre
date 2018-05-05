import time
import datetime

# 打印当前时间戳
print(time.time())

# 转换时间戳为时间元组struct
print(time.localtime(time.time()))

# 格式化想要输出的时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d"))

# datatime模块实现
t = time.time()
datetime.datetime.fromtimestamp(t).strftime("Y-%m-%d %H:%M:%S")

datetime.datetime.now().strftime("%Y")
datetime.datetime.today().strftime("%Y")
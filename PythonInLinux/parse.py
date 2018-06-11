# import configparser

# p = configparser.ConfigParser(allow_no_value=True)
# print("读取配置文件", p.read("./config.ini"))
# print("返回所有章节列表", p.sections())
# print("判断章节是否存在", p.has_section("client"))
# print("返回一个章节下所有选项的列表", p.options("client"))
# print("判断一个选项是否存在", p.has_option("client", "user"))
# print("获取选项的值", p.get("client", "host"))
# print("获取选项的值，以int类型返回", p.getint("client", "port"))

import sys
import configparser

p = configparser.ConfigParser(allow_no_value=True)
print("读取配置文件", p.read("./config.ini"))
print("删除一个章节", p.remove_section("client"))
print("添加一个章节", p.add_section("mysql"))
print("添加一个选项", p.set("mysql", "host", "localhost"))
print("添加一个选项", p.set("mysql", "port", "3306"))
print("写入到为文件", p.write(sys.stdout))

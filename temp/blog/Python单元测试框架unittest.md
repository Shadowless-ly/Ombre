# Python单元测试框架unittest

Python单元测试框架unittest最初灵感来自于JUnit，与其他语言的主要单元测试框架有相似的风格。它支持自动化测试，共享设置和闭合代码测试，聚合测试，以及从报告框架上进行独立测试。

## unittest概念

unittest在面向对象方法上支持的一些重要概念:

1. **测试夹具（test fixture）**

   一个**测试夹具**表示一个或多个测试，以及任何相关的清理和准备工作。

2. **测试用例（test case）**

   **测试用例**是一个单独的测试单元，它检查对特定输入集的特定响应。unittest提供了基类TestCase用以创建新的**测试用例**。

3. **测试套件（test suite）**

   **测试套件**是测试用例，其他**测试套件**的集合，用于聚合需要一起执行的测试。

4. **测试执行器（test runner）**

   用来执行测试用例，其中run会执行TestSuite/TestCase中的run(result)方法。**测试执行器**可以使用图形接口，文字接口或返回一个特定的值来表明测试的执行结果。

   

## 基本使用

```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
    
def main():
    unittest.main()

if __name__ == '__main__':
    main()
    
```

通过继承`unittest.TeatCase`创建一个测试用例，三个单独的测试方法以字母test开头。这是一个约定的命名规则，用以指示测试执行类中那个方法代表测试用例。

执行结果如下：
```bash
on stringtest.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

可以在命令行中加入`-v`参数来显示详细信息:

```bash
shadowless@shadowless-PC:~/Desktop/program/Ombre/core_python/pyunittest$ python stringtest.py -v
test_isupper (__main__.TestStringMethods) ... ok
test_split (__main__.TestStringMethods) ... ok
test_upper (__main__.TestStringMethods) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```

## 命令行接口

我们可以在命令行直接运行测试用力模块，测试用例，测试项。

```bash
python -m unittest stringtest
python -m unittest stringtest.TestStringMethods
python -m unittest stringtest.TestStringMethods.test_upper
```

当使用`python -m unittest`时不附加任何参数，表示使用Test Discovery。
所有帮助信息可以使用`python -m unittest -h`查看。

### 命令行参数

* -b, --buffer
测试运行时标准输出，标准错误输出的缓冲区大小。一般pass不需要输出，当测试失败或出现错误时会有相应的错误信息。
* -c, --catch
`Control-C`组合键，在第一次时会等待当前测试完成，返回到此为止的所有测试结果。再次按下则直接触发KeyboardInterrupt 异常。
* -f, --failfast
在出现第一个错误时停止测试。
* --locals
在tracebacks中打印所有变量值。

## 测试用例发现
unittest可以自动识别测试用例，所有测试用例必须是模块或者包，且可以从top-level目录直接import（意味着文件名时合法标识符）。
测试用例发现功能使用`TestLoader.discover()`实现，但也可以直接在命令行使用：

```bash
python -m unittest discovery
# 该命令等同于python -m unittest
# discovery支持命令行参数如下:
# -v, --verbose:显示详细输出
# -s, --start-directory <directory>:开始查找的目录，默认为当前目录.
# -p, --pattern <pattern>:匹配文件的模式，默认为test*.py
# -t, --top-level-directory directory:项目的最顶层目录，默认为开始目录

# 其中-s, -p, -t可以作为位置参数，以下效果相同:
python -m unittest discover -s project_directory -p "*_test.py"
python -m unittest discover project_directory "*_test.py"

```
## 组织测试代码





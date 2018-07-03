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
       
    
```




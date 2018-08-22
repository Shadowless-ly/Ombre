//golang以包为管理单位
//每个文件必须先声明包
//程序必须有一个main包
package main

import "fmt"

//入口函数
func main() { //左括号必须和函数名同行
	fmt.Println("hello go") //Println自动换行
	datatype()
}

func test_return () (a, b, c int){
	return 1, 2, 3
}

func datatype() {
	//告诉编译器以多大内存存储
	//变量名规范:字母数字下划线，不能数字开头，不能关键字，区分大小写
	//1. 声明:var 变量名 类型
	//2. 只声明，未初始化的变量默认值为0
	//3. 同一个{}内，声明的变量名唯一
	// var a int

	//4. 可以同时声明多个变量
	var a, c int //初始化
	a = 10	//赋值
	c = 20
	var b int = 10  //5. 初始化同时赋值
	d := 30	//6. 自动推导类型，必须初始化，通过初始化的值确定类型(先声明后赋值)
	fmt.Println("var:", a, c, b, d)
	// d := 20 //7. 不能重复使用自动推导类型，因为包含新建变量的动作
	fmt.Printf("a=%d, b=%d, c=%d\n", a, b, c)

	a, _, c = test_return()
	fmt.Printf("a=%d, b=%d, c=%d\n", a, b, c)
}
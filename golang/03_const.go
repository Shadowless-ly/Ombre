package main

import "fmt"

func main() {
	//常量的声明需要使用const关键字
	const a int = 10
	fmt.Println("a=", a)
	//	a = 20 //常量不允许赋值
	const b = 10.01 //const do not need :=
	fmt.Printf("b type is %T\n", b)
	fmt.Println("b=", b)
}

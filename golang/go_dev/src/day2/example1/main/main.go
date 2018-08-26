package main

import (
	"fmt"
	a "day2/example1/add"
)

func main() {
	fmt.Printf("name is %s\n", a.Name)
	fmt.Printf("number %d \n", a.Number)
}

//每个源文件都可以包含一个init函数，在main之前被调用
func init() {
	fmt.Println("main init")
}
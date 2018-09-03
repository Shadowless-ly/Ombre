package main

import (
	"fmt"
)

func factorial(n int) int {
	var ret = 1
	for i := 1; i <= n; i++ {
		ret = ret * i
		// fmt.Println(ret)
	}
	return ret
}

func factorialAdd(n int) int {
	ret := 0
	for i := 1; i <= n; i++ {
		ret += factorial(i)
	}
	return ret
}

func main() {
	fmt.Println(factorialAdd(10))
}

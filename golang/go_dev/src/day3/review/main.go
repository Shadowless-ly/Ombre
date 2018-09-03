package main

import "fmt"

func modify(n *int) {
	fmt.Println("in modify function,", n)
	*n = 100
}

func main() {
	var n int
	fmt.Println("out modify function,", &n)
	modify(&n)
	fmt.Println(n)
}

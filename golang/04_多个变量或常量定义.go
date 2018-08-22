package main

import "fmt"

func main() {
	//	var a int
	//	var b float64
	var (
		a int
		b float64
	)
	a, b = 10, 3.14
	fmt.Println("a =", a)
	fmt.Println("b =", b)

	const (
		//		i int     = 10
		i         = 10 //auto get type
		j float64 = 3.14
	)
	fmt.Println("i =", i)
	fmt.Println("j =", j)
}

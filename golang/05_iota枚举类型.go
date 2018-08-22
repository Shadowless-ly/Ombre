package main

import "fmt"

func main() {
	const (
		a = iota //0
		b = iota //1
		c = iota //2
	)
	fmt.Printf("a = %d, b = %d, c = %d\n", a, b, c)

	//	when get const ,iota return to 0
	const d = iota
	fmt.Printf("d = %d\n", d)

	// could only write one iota
	const (
		a1 = iota //0
		b1
		c1
	)
	fmt.Printf("a1 = %d, b1 = %d, c1= %d\n", a1, b1, c1)

	//the value be same when at same line
	const (
		i          = iota
		j1, j2, j3 = iota, iota, iota
		k          = iota
	)
	fmt.Printf("i = %d, j1 = %d, j2 = %d, j3 = %d, k = %d\n", i, j1, j2, j3, k)
}

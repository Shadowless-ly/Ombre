package main

import (
	"fmt"
)

func exchange(a *int, b *int) {
	*a, *b = *b, *a
}

func main() {
	num_1 := 1
	num_2 := 2
	fmt.Println("num_1 =", num_1, "num_2 =", num_2)
	exchange(&num_1, &num_2)
	fmt.Println("num_1 =", num_1, "num_2 =", num_2)
}
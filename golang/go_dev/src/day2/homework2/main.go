package main

import (
	"fmt"
)

func pow(x, n int) int {
	ret := 1
	for n != 0 {
		ret = ret * x
		n--
	}
	return ret
}

func main() {
	for i := 100; i <= 999; i++ {
		number1 := i - i%100
		number2 := i - number1 - (i-number1)%10
		number3 := i - number1 - number2
		// fmt.Println(i, number1/100, number2/10, number3)
		if (pow(number1/100, 3) + pow(number2/10, 3) + pow(number3, 3)) == i {
			fmt.Println(i)
		}
	}
}

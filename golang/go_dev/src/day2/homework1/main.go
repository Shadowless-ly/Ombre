package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	var m int
	fmt.Scanf("%d %d", &n, &m)
	var numArray []int
	for i := n; i <= m; i++ {
		count := 0
		for j := 2; j <= int(math.Sqrt(float64(i))); j++ {
			if i%j == 0 {
				count++
			}
		}
		if count == 0 {
			numArray = append(numArray, i)
			println("素数:", i)
		}
	}
	fmt.Printf("共有%d个素数!\n", len(numArray))
}

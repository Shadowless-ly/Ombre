package main

import (
	"fmt"
	"time"
)

const (
	Female = 2
	Man = 1
)

func main() {
	second := time.Now().Unix()
	fmt.Println(second)
	if (second % Female == 0) {
		fmt.Println("Female")
	} else {
		fmt.Println("man")
	}

}
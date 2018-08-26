package main

import (
	. "fmt"
	"time"
)

var value int

func main() {
	c := make(chan int, 1)
	go add_it(3, 5, c)
	get := <- c
	Println("get:", get)
	Println(double_ret(100, 200))
	_, num := double_ret(11,22)
	Println(num)
	Scanf("1")
	// Printf("%s, %d, %T", time.Second, time.Second, time.Second)
	// for i := 0; i<= 100; i++ {
	// 	go go_test(i)
	// }
	// time.Sleep(time.Second)
	// go test_pipe()
	// test_lock()
}

func go_test(i int) {
	Println(i)
	time.Sleep(1000000000)
}

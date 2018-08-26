package main

import (
	"fmt"
	"time"
)

// 使用管道实现多个goroute之间通过channel进行通信
// 公共变量为大写，可以被其他包直接引用，私有变量为小写

func test_pipe() {
	pipe := make(chan int, 3)
	pipe <- 1
	pipe <- 2
	pipe <- 3

	var t1 int
	t1 = <-pipe
	pipe <- 4
	value = <-pipe
	pipe <- 5
	fmt.Println(pipe, t1)
	fmt.Println("value", value)
}

func test_lock() {
	time.Sleep(time.Second * 5)
}

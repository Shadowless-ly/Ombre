package main
/*
包名为main编译为可执行文件
不为main编译成lib库
*/

import (
	"fmt"
	"time"
	"math/rand"
)


func main(){
	// 管道
	// pipe := make(chan int,3)
	// goroute
	tell_add_to_n(100)
	// go productor(pipe)
	// go consumer(pipe)
	// time.Sleep(time.Second*100)
}

func productor(pipe chan int) {
	for i:=0;i<=100;i++ {
		pipe <- i
		sleepnum := rand.Intn(5)
		time.Sleep(time.Second*time.Duration(sleepnum))
	}
}

func consumer(pipe chan int) {
	for i := <- pipe;i<=100;i = <- pipe {
	fmt.Printf("GET number: %d\n", i)
	}
}


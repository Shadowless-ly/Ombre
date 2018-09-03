package main

import . "fmt"

var a string


func main() {
	a := "G"
	Print(a)
	f1()
	var b int8 = 100
	var c int16 = int16(b)
	_ = c
}

func f1() {
	a := "O"
	Println(a)
	f2()
}

func f2() {
	Print(a)
}
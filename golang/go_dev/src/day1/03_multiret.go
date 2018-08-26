package main

func add_it(a int , b int, c chan int) (int) {
	var value int
	value = a + b
	c <- value
	return 0
}


func double_ret(number1 int, number2 int) (int, int) {
	return number1*2, number2*2
}
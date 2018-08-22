package main

import . "fmt"

/*
type 	    length 	default  comment
bool 	      1		 false	true or false
byte	      1		 0		uint8
rune	      4		 0		unicode, uint32
int,uint	 4,8	 0		32bit,64bit
int8,uint8	  1		 0      -128~127,0~255
int16,uint16  2      0      -32768~32767,0~65535
int32,uint32  4      0      -21e8~21e8,0~42e8
int64,uint64  8		 0
float32		  4      0.0    0.0000001
float64		  8      0.0    1e-15
complex64     8
complex128	  16
uintptr		  4,8			uint32,uint64
string				 ""		utf-8
*/

func test_bool() {
	var a bool
	a = true
	Println("a =", a)

	var b bool
	b = false
	Println("b =", b)

	c := false
	Println("c =", c)

	var d bool
	Println("defalut value:", d)
}

func test_float() {
	var f1 float32
	f1 = 3.14
	Println("f1 =", f1)

	f2 := 3.14
	Printf("f2 type is %T\n", f2)
}

func chacatar_test() {
	var ch byte
	var ch_upper byte
	ch = 97
	ch_upper = 'A'
	Printf("ch = %c, %d\n", ch, ch)
	Printf("ch_upper = %c, %d\n", ch_upper, ch_upper)
	Print("111\n")
}

func string_test() {
	var stra string
	stra = "abc"
	strb := "123"
	Printf("%s, %s\n", stra, strb)
	Printf("%s, %d\n", stra, len(stra))
}

func main() {
	test_bool()
	test_float()
	chacatar_test()
	string_test()
}

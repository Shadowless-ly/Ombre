package main

import (
	"fmt"
)

func reverse(str string) string {
	var result string
	strLen := len(str)
	for i := 0; i < strLen; i++ {
		result = result + fmt.Sprintf("%c", str[strLen-i-1])
	}
	return result
}

func reverse1(str string) string {
	// 转换为字符数组
	var result []byte
	tmp := []byte(str)
	length := len(str)
	for i := 0; i < length; i++ {
		result = append(result, tmp[length-i-1])
	}
	return string(result)
}

func main() {
	var str1 = "hello"
	str2 := "world"

	// str3 := str1 + " " + str2
	str3 := fmt.Sprintf("%s %s", str1, str2)
	n := len(str3)
	fmt.Printf("len(str3)=%d\n", n)
	fmt.Println(str3[:5])

	fmt.Println(str3[6:])

	fmt.Println(reverse(str3))
	fmt.Println(reverse1(str3))
}

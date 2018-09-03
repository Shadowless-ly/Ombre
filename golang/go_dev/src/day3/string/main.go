package main

import (
	"fmt"
	"strings"
)

/*
string和strconv的使用

strings.Index str在s中第一次出现的位置
strings.LastIndex str在s中最后一次出现的位置
strings.Replace(str string, old string, new string, n)替换
strings.Count(str string, substr string) int:计数
strings.Repeat(str string, count int) string:重复count次
strings.ToLower(str string) string:转为小写
strings.ToUpper(str string) string:转为大写
strings.trimSpace(str string) 去掉字符串首尾空格
strings.Trim(str string, cut string) 去掉字符串首尾cut字符
strings.TrimLeft(str string, cut string) 去掉字符串首cut字符
strings.TrimRight(str string, cut string) 去掉字符串末cut字符
strings.Field(str string) 返回str空格分隔的所有子串的slice
string.Split(str string, split string) 返回str用split分隔的所有子串的slice
strings.Join(s1 []string, sep string) 用sep把s1中的所有元素连接起来
strings.Itoa(i int) 把一个整数i转换成字符串
strings.Atoi(str string)(int error) 把一个字符串转换为整数
*/

func prefix(s string) {
	if strings.HasPrefix(s, "go") {
		fmt.Println("has prefix \"go\"")
	} else {
		fmt.Println("do not have prefix \"go\"")
	}
}

func urlProcess(url string) string {
	result := strings.HasPrefix(url, "http://")
	if !result {
		url = fmt.Sprintf("http://%s", url)
	}
	return url
}

func pathProcess(path string) string {
	result := strings.HasSuffix(path, "/")
	if !result {
		path = fmt.Sprintf("%s/", path)
	}
	return path
}

func main() {
	var (
		url  string
		path string
	)
	fmt.Scanf("%s%s", &url, &path)
	url = urlProcess(url)
	path = pathProcess(path)
	fmt.Println(url)
	fmt.Println(path)
}

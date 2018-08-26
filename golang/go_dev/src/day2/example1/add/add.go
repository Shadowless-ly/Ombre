package add


import (
	"fmt"
)
// 编译过程中已经赋值
var Name string = "shadowless"
var Number int = 100

func init(){
	fmt.Println("test init")
}
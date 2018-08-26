package main

/*
所有源码以.go结尾
字母下划线开头，大小写敏感
_空白符，接受多值返回

break
default
func
interface
select
case
defer
go
map
struct
chan
else
goto
package
switch
const
fallthough
if
range
type
continue
for
import
return
var
*/
import (
	"fmt"
)
/*
同一个包中的函数直接调用
不同包中的函数，通过包名+点+函数名调用
大写意味着函数/变量可以导出
小写不能导出，为私有，包外部不能访问
*/

func tell_add_to_n(n int) (i int, j int){
	for i:=0;i<=n;i++{
		fmt.Printf("%d + %d = %d\n", i, n-i, n)
	}
	return
}
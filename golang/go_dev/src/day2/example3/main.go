package main

import (
	"fmt"
	"os"
)

func main() {
	var goos string = os.Getenv("OS")
	fmt.Printf("The operation system is %s\n", goos)
	path := os.Getenv("PATH")
	fmt.Printf("PATH is %s\n", path)
	fmt.Println(os.Getenv("GOPATH"))
}

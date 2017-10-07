package main

import (
	"testing"
	"fmt"
)

func wiggleSort(nums []int)  {
    if len(nums) <= 1 {
        return
    }
    for i, _ := range nums[:len(nums)-1] {
        a, b := nums[i], nums[i+1]
        if i%2 == 0 {
            if a > b {
                nums[i], nums[i+1] = b, a
            }
        } else {
            if a < b {
                nums[i], nums[i+1] = b, a
            }
        }
    }
}

func TestWiggleSortBasic(t *testing.T) {
	fmt.Println("testing")
}

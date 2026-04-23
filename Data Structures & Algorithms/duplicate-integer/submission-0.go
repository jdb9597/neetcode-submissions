func hasDuplicate(nums []int) bool {
    numsCount := make(map[int]int)
    for _, val := range nums {
       _, foundDup := numsCount[val] 
       if foundDup{
        return true
       }
       numsCount[val] = 1
    }
    return false;
}

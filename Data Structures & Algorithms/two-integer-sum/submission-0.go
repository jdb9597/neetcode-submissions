func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
	for i, v := range nums {
		diff := target - v
		if idx, ok := seen[diff]; ok {
			return []int{idx, i}
		} else {
			seen[v] = i
		}
	}
    return nil
}

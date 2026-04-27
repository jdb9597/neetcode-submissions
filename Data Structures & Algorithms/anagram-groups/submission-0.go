func groupAnagrams(strs []string) [][]string {
    freqmap := make(map[[26]int][]string)
    for _, str := range strs {
        freq := [26]int{}
        for _, ch := range str {
            freq[ch - 'a']++

        }
        freqmap[freq] = append(freqmap[freq], str)
    }
    result := [][]string{}
    for _, v := range freqmap {
        result = append(result, v)
    } 
    return result
}


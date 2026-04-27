func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }
    sFreq := make(map[rune]int)
    tFreq := make(map[rune]int)
    for _, char := range s {
        sFreq[char] += 1
    }
    for _, char := range t {
        tFreq[char] += 1
    }
    for k, v := range sFreq {
        if tFreq[k] != v {
            return false
        }
    }
    return true
}
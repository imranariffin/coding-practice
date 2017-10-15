import "fmt"

func isAnagram(s string, t string) bool {
    sc := make(map[string]int)
    tc := make(map[string]int)
    for _, c := range s { sc[string(c)]++ }
    for _, c := range t { tc[string(c)]++ }
    if len(tc) != len(sc) { return false }
    for c, count := range sc { 
        if tc[c] != count { return false } 
    }
    return true
}

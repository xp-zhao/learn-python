def findAnagrams(s: str, p: str) -> list[int]:
    res = []
    need = {i: p.count(i) for i in p}
    window = {}
    left, right, valid = 0, 0, 0
    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
        while right - left >= len(p):
            if valid == len(need):
                res.append(left)
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] = window[d] - 1
    return res

print(findAnagrams('cbaebabacd', 'abc'))
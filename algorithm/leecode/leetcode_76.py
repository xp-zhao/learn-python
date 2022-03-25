def minWindow(s: str, t: str):
    need = {i: t.count(i) for i in t}
    window = {}
    left, right, valid = 0, 0, 0
    start, size = 0, float('inf')
    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
        while valid == len(need):
            if right - left < size:
                start = left
                size = right - left
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] = window.get(d) - 1
    return '' if size == float('inf') else s[start:right]


print(minWindow('ADOBECODEBANC', 'ABC'))

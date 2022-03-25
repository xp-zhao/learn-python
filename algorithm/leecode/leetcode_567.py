from numpy import true_divide


def checkInclusion(t: str, s: str) -> bool:
    need = {i: t.count(i) for i in t}
    window = {}
    left, right, valid = 0, 0, 0
    while right < len(s):
        c = s[right]
        right += 1
        if c in need:
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1
        while right - left >= len(t):
            if valid == len(need):
                return True
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:
                    valid -= 1
                window[d] = window[d] - 1
    return False

print(checkInclusion('ab', 'dba'))
print(checkInclusion('ab', 'dbb'))

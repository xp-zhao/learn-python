def lengthOfLongestSubstring(s: str) -> str:
    window = {}
    left, right, res = 0, 0, 0
    while right < len(s):
        c = s[right]
        right += 1
        window[c] = window.get(c, 0) + 1
        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] = window[d] - 1
        res = res if res > right - left else right - left
    return res

print(lengthOfLongestSubstring('bbbbb'))
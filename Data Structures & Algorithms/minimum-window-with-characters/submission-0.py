class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        window = {}

        left = 0
        have = 0
        need_len = len(need)
        res = [-1, - 1]
        res_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_len:
                window_size = right  - left + 1
                if window_size < res_len:
                    res_len = window_size
                    res = [left, right]
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
        l,r = res
        return "" if res_len == float("inf") else s[l:r+1]


      


        
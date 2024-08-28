class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len, hashmap = 0, {}
        start = 0
        for end in range(len(s)):
            tail = s[end]
            hashmap[tail] = hashmap.get(tail, 0) + 1
            if len(hashmap) <= 2:
                max_len = max(max_len, end - start + 1)
            while len(hashmap) > 2:
                head = s[start]
                hashmap[head] -= 1
                if hashmap[head] == 0:
                    del hashmap[head]
                start += 1
        return max_len
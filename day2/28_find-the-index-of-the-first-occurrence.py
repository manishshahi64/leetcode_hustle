class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) +1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

haystack = "iseman"
needle = "man"
p1 = Solution()
print(p1.strStr(haystack,needle))
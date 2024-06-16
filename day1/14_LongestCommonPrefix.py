class Solution:
    def longestCommonPrefix(self, strs) -> str:
        val = ""
        strs.sort()
        firts=strs[0]
        last=strs[-1]
        for i in range(min(len(firts),len(last))):
            if firts[i] != last[i]:
                return val  
            val+=firts[i]
        return val
        
p1 = Solution()
print(p1.longestCommonPrefix(["dog","racecar","car"]))
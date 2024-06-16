class Solution:
    def isValid(self, s: str) -> bool:
        mydict = {
            "(" : ")",
            "{": "}",
            "[": "]"
            }
        val = []
        for i in s:
            if i in mydict:
                val.append(i)
            elif  len(val) == 0 or i != mydict[val.pop()]:
                return False
        return len(val) == 0

p1 = Solution()
print(p1.isValid("()[]]"))
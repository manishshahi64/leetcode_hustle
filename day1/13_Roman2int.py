class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict ={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        val = 0
        S = s.replace("IV","IIII").replace("IX","VIIII").replace("XL","XXXX").replace("XC","LXXXX").replace("CD","CCCC").replace("CM","DCCCC")
        for i in S:
            val+=my_dict[i]
        return val
s = "MCMXCIV"
p1 = Solution()

print(p1.romanToInt(s))
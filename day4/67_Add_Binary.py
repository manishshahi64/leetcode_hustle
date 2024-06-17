# Rememeber
# 1+1=0 with carry 1
# 1+0=1 with carry 0
# 0+1=1 with carry 0
# 0+0=0 with carry 0
# Imp:1+1=1 with carry 1 if previous carry was 1.
# The carry gets added in next step(scanning from right to left).
####

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i>=0 or j>=0 or carry:
            if i>=0:
                carry += int(a[i])
                i-=1
            if j>=0:
                carry += int(b[j])
                j-=1
            s.append(str(carry%2))
            carry//=2
        return "".join(reversed(s))


a = "1011"
b = "1101"
p1 = Solution()
print(p1.addBinary(a,b))
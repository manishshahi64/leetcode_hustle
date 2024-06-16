class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = s.split(" ")
        mylist = []
        for i in y:
            if i != "":
                mylist.append(i)
        return len(mylist[-1])
s="   fly me   to   the moon  "
p1 = Solution()
print(p1.lengthOfLastWord(s))
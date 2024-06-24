class Solution:
    def climbStairs(self, n: int) -> int:
        my_list = [0,1,2]
        for i in range(3,n+1):
            my_list.append(my_list[i-1] + my_list[i-2])
        return my_list[n]

n = 20
p1 = Solution()
print(p1.climbStairs(n))
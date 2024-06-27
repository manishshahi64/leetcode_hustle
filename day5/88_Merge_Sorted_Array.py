class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        nums1 = (self.while_func(nums1,m) + self.while_func(nums2,n))
        nums1.sort()
        return nums1
    def while_func(self,num,x):
        while len(num)!=x:
            num.pop(x)
        return num

################ or ################### 

        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()
        return nums1
    
p1 = Solution()
print(p1.merge([1,2,3,0,0,0],3,[2,5,6],3))
        
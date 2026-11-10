class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculating prefix
        prefix = 1
        p = [1]*len(nums)
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            p[i] = prefix
        
        # calculating suffix 
        suffix = 1
        s = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            suffix *= nums[i+1]
            s[i] = suffix
        
        res = []
        for i in range(len(nums)):
            ans = p[i]*s[i]
            res.append(ans)
        
        return res
        
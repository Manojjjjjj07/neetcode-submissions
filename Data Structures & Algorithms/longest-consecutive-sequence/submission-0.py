class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0
        for num in nums:
            count = 0
            if num-1 not in numset:
                x = num
                count = 1
                while x+1 in numset:
                    count += 1
                    x += 1
                
                maxcount = max(maxcount, count)
                
        return maxcount
                
        
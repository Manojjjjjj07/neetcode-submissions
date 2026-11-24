class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxarea = 0

        left, right = 0, n-1
        while left<=right:
            width = right - left
            height = min(heights[left], heights[right])
            maxarea = max(maxarea, width*height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxarea
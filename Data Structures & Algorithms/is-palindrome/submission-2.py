class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n-1
        while left<=right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower()==s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False

        return True
        
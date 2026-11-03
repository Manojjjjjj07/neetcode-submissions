from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for ch in strs:
            freq = [0]*26
            for char in ch:
                index = ord(char) - ord('a')
                freq[index] += 1
            words[tuple(freq)].append(ch)

        res = []
        for value in words.values():
            res.append(value)
        
        return res

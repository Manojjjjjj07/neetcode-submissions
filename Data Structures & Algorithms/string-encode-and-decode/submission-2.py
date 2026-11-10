class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for ch in strs:
            res.append(chr(len(ch)))
            res.append(ch)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index<len(s):
            count = ord(s[index])
            start = index + 1
            word = s[start:start+count]
            res.append(word)
            index = start + count
        return res
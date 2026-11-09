class Solution:


    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            encoded = chr(len(word))+word
            res += encoded
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        index = 0
        while index<len(s):
            count = ord(s[index])
            word = ""
            start = index+1
            for i in range(start,start+count):
                word += s[i]
            
            res.append(word)
            index = start + count
        return res

class Solution:
    def __init__(self):
        self.length = []
    def encode(self, strs: List[str]) -> str:
        res = []
        for ch in strs:
            self.length.append(len(ch))
            res.append(ch)
            res.append("#")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        word_length_index = 0
        index = 0
        while index<len(s):
            length = self.length[word_length_index]
            word = s[index:index+length]
            res.append(word)
            word_length_index += 1
            index = index + length + 1
        
        return res

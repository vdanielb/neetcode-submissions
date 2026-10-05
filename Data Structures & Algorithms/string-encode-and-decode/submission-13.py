class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lengths = ""
        for strng in strs:
            lengths += str(len(strng))
            lengths += ","
        return lengths + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        pointer = 0
        lengths=[]
        while s[pointer] != "#":
            curr = ""
            while s[pointer] != ",":
                curr += s[pointer]
                pointer += 1
            lengths.append(int(curr))
            pointer+=1
        
        res = []
        pointer +=1 
        for length in lengths:
            res.append(s[pointer:pointer+length])
            pointer += length
        return res
            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        curSeq = set()
        longest = 0
        while r<len(s):
            ch = s[r]
            if ch not in curSeq:
                curSeq.add(ch)
                r+=1
            else:
                while ch in curSeq:
                    curSeq.remove(s[l])
                    l+=1
            longest = max(longest,r-l)
        return longest
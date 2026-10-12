class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxf = s[0]
        counts = defaultdict(int)
        l=0
        res = 0
        for r in range(n):
            counts[s[r]] += 1
            if counts[s[r]] > counts[maxf]:
                maxf=s[r]
            if r-l+1-counts[maxf] > k:
                counts[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)

        return res


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        all_letters = "qwertyuiopasdfghjklzxcvbnm"
        s1_counts = {letter:0 for letter in all_letters}
        s2_counts = {letter:0 for letter in all_letters}
        for ch in s1:
            s1_counts[ch] += 1
        
        l = 0
        r = len(s1)-1
        for ch in s2[l:r+1]:
            s2_counts[ch] += 1

        matches = 0
        for ch in s1_counts:
            matches += (1 if s1_counts[ch] == s2_counts[ch] else 0)
        if matches == 26:
            return True

        while r<len(s2)-1:
            r+=1
            s2_counts[s2[r]] += 1
            if s2_counts[s2[r]] == s1_counts[s2[r]]:
                matches += 1
            if s2_counts[s2[r]] - 1 == s1_counts[s2[r]]:
                matches -=1
            
            if s2_counts[s2[l]] == s1_counts[s2[l]]:
                matches -=1
            if s2_counts[s2[l]] - 1 == s1_counts[s2[l]]:
                matches += 1
            s2_counts[s2[l]] -= 1   
            l+=1
            if matches == 26:
                return True

        return matches == 26
             
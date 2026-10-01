class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        counts_sorted = (sorted(counts.items(), key=lambda x: x[1]))
        res = []
        for counts in counts_sorted[:-k-1:-1]:
            res.append(counts[0])
        return res
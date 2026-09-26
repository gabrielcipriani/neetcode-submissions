class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        top = []
        for num in nums:
            count[num] += 1
        for i in range(k):
            key, value = (max(count.items(), key=lambda item: item[1]))
            top.append(key)
            count.pop(key)
        return top

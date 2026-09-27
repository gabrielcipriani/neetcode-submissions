class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        count_groups = [[] for _ in range(len(nums) + 1)]  

        for num, freq in count.items():
            count_groups[freq].append(num)

        top = []

        for i in range(len(nums), 0, -1):
            for num in count_groups[i]:
                top.append(num)
                if len(top) == k:
                    return top



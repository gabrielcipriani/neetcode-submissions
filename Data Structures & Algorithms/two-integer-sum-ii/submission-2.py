class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        found = False
        p1=0
        p2=len(numbers)-1
        while not found:
            total = numbers[p1] + numbers[p2]
            if total == target:
                return [p1+1, p2+1]
            elif total > target:
                p2 -= 1
            elif total < target:
                p1 += 1


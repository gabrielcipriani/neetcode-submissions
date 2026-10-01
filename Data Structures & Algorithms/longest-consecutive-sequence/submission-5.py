class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    seen = set(nums)

    # guard clause
    if len(seen) == 0:
      return 0

    total = 0

    for num in nums:
      if num - 1 in seen:
        continue
      else:
        start = num
        temp_total = 1
        while True:
            if (start + 1) in seen:
                temp_total += 1
                start += 1
            else: 
                break
        if temp_total > total:
            total = temp_total

    return total

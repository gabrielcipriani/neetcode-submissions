class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    seen = set(nums)

    # guard clause
    if len(seen) == 0:
      return 0

    start = None
    total = 0

    for i in range(len(nums)):
      if nums[i]-1 in seen:
        continue
      else:
        start = nums[i]
        temp_total = 1
        while True:
            if (start + 1) in seen:
                temp_total += 1
                start += 1
            else: 
                start = None
                break
        if temp_total > total:
            total = temp_total

    return total

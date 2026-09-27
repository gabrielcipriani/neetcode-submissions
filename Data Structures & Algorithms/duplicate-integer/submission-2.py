class Solution:
  def hasDuplicate(self, nums: list[int]) -> bool:
    setNums = set()
    for n in (nums):
      if n in setNums:
        return True
      setNums.add(n)
    return False
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      products = [0] * len(nums)
      left = [] # product of everything before i

      for i in range(len(nums)):
        if i == 0:
          left.append(1)
        else:
          left.append(left[i-1]*nums[i-1])

      for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
          right_product = 1
        else:
          right_product *= nums[i+1]

        products[i] = left[i] * right_product

      return products

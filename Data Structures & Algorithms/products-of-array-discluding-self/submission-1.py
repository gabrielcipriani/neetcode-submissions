class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      products = []

      for i in range(len(nums)):
        if i == 0:
          products.append(1)
        else:
          products.append(products[i-1]*nums[i-1])

      for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1:
          right_product = 1
        else:
          right_product *= nums[i+1]

        products[i] *= right_product

      return products
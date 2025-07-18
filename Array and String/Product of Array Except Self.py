class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        res = [1] * n

        prefix = 1  # left_product
        

        for i in range(n):

            res[i] *= prefix
            prefix *= nums[i]
        
        postfix = 1  # right_product or suffix

        for i in range(n - 1, -1, -1):

            res[i] *= postfix
            postfix *= nums[i]

        return res

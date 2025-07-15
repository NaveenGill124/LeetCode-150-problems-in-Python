class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        #without using extra space

        #using slicing

        nums.reverse()

        nums[:k] = reversed(nums[:k])
        
        nums[k:] = reversed(nums[k:])




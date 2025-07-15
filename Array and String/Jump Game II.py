class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        num_jump = 0
        max_reach = 0
        curr_end_jump = 0

        for i in range(n-1):

            max_reach = max(max_reach, i + nums[i])

            if i == curr_end_jump:

                num_jump += 1
                curr_end_jump = max_reach
            
        
        return num_jump

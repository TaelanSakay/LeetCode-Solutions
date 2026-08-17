class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        operations = 0
        l, r = 0, len(nums) - 1

        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum == k:
                operations += 1
                l += 1
                r -= 1
            elif current_sum < k:
                l += 1  
            else:
                r -= 1 

        return operations

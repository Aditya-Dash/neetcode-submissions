class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumSolution(nums, target)

    def twoSumSolution(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            num2 = target - num
            if num2 in nums[idx+1:]:
                return [idx, nums.index(num2, idx + 1)]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSumSolution(nums, target)

    def twoSumSolution(self, nums: List[int], target: int) -> List[int]:
        """
        Analysis Result
        Time complexity: O(n^2) in the worst case. 
        For each element, the code checks membership of the remaining sublist (which is O(n)) 
        and the index call can also be O(n) in the worst case, leading to quadratic behavior.

        Space complexity: O(1) auxiliary space, aside from the input list, since it uses a 
        few local variables and slices that allocate new lists (the slice nums[idx+1:] 
        creates a new list of up to n elements, which technically makes it O(n) extra space in Python; 
        without counting that slice creation, the extra space is O(1)).
        """

        for idx, num in enumerate(nums):
            num2 = target - num
            if num2 in nums[idx+1:]:
                return [idx, nums.index(num2, idx + 1)]

    def twoSumSolutionOptimized(self, nums: List[int], target: int) -> List[int]:

        """
        Time complexity: O(n^2) in the worst case. 
        The for loop iterates n times, and for each iteration the expression nums[idx+1:] 
        creates a new sublist (O(n)) and the in operator checks membership (which is O(n) in the sublist),
        leading to overall quadratic behavior. Additionally, nums.index(...) is O(n) in the worst case.

        Space complexity: O(n) due to creating the sliced sublist nums[idx+1:]. The rest uses O(1) auxiliary space.
        """
        for idx, num in enumerate(nums):
            num2 = target - num
            if num2 in nums[idx+1:]:
                return [idx, nums.index(num2, idx + 1)]
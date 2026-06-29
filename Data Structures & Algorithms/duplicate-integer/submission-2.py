class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return self.hasDuplicateSolution(nums)
        return self.hasDuplicateSolutionOptimized(nums)

    def hasDuplicateSolution(self, nums):
        return not len(set(nums)) == len(nums)

    def hasDuplicateSolutionOptimized(self, nums):
        numset = set()
        for num in nums:
            if num in numset:
                return True
            numset.add(num)

        return False
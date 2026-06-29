class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #return self.hasDuplicateSolution(nums)
        #return self.hasDuplicateSolution_appoach2(nums)
        return self.hasDuplicateSolutionOptimized(nums)

    def hasDuplicateSolution(self, nums):
        return not len(set(nums)) == len(nums)

    def hasDuplicateSolutionOptimized(self, nums):
        """"
        between building progressively a set and early returning vs letting the engine build the whole set, 
        complexity is kind of the same, it's more in the logic that building the set wins because of short-circuiting here
        Time complexity: O(n)O(n)
        Space complexity: O(n)O(n)
        """

        numset = set()
        for num in nums:
            if num in numset:
                return True
            numset.add(num)
        return False

    def hasDuplicateSolution_appoach2(self, nums: list) -> bool:
        """
        Complexity BreakdownSpace Complexity: O(1). 
        No new arrays, sets, or hash maps are created.
         The comparison happens directly within the existing memory allocation.
         Time Complexity: O(N log N). Sorting an array of length N takes O(N log N) time, 
         which makes this approach slower than your original O(N) set solution.

        """
        nums.sort()  # Sorts the list in place (modifies original list)
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:  # Check adjacent elements
                return True
                
        return False
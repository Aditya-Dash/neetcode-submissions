class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return self.isAnagramSolution(s, t)
        return self.isAnagramOptimized(s, t)

    def isAnagramSolution(self, s: str, t: str) -> bool:
        """
        Time complexity: O(n log n) due to sorting both strings of length n. 
        Space complexity: O(n) for the two auxiliary lists created from the strings.
        """
        s1= list(s)
        s1.sort()
        t1= list(t)
        t1.sort()
        return s1 == t1

    def isAnagramOptimized(self, s: str, t: str) -> bool:
        """
        Analysis Result
        Time complexity: O(n), where n is the length of the strings 
        (both s and t, since lengths are equal after the initial check). 
        Building two counters takes O(n) time, and comparing two dictionaries is 
        O(k) where k is the number of distinct characters (k ≤ n).

        Space complexity: O(k), due to storing the counts of distinct characters 
        in the two Counter objects (in the worst case, k equals the size of the character 
        set, e.g., O(n) if all characters are unique)."""
        if len(s) != len(t):
            return False
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        return count_s == count_t
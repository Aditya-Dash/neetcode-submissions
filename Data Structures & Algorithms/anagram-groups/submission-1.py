class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.groupAnagramsSolutions(strs)
    
    def groupAnagramsSolutions(self, strs: List[str]) -> List[List[str]]:
        """

        Analysis:
        - Each string st of length k is converted to a list, sorted, and joined back to form a key. 
          Sorting a string of length k takes O(k log k) time. This is done for every string, so for n strings
          with average length k, the total sorting time is O(n k log k).
        - The rest of the operations (list creation, dictionary lookups, and appends) are O(k) per string 
          for the character handling, but dominated by the sorting step.
        - Building the resulting groups involves iterating over n strings and appending to lists, which is 
          O(n) additional work, plus the total memory used for the keys and groups.

        Space complexity:
        - The dictionary rdict stores one key per distinct anagram class. Each key is a sorted version of a
          string, length k, so overall O(nk) space in the worst case (if all strings are distinct anagrams, 
          keys total length sum is O(nk)).
        - The values in the dictionary store all original strings, totaling O(nk) space as well.
        - The additional space for temporary list and string conversions per string is O(k), but not accumulated 
          beyond the current iteration.

        Overall:
        - Time complexity: O(n k log k), where n is the number of strings and k is the average length of the strings.
        - Space complexity: O(n k) in the worst case.
        """
        if len(strs) == 1:
            return [strs]
        
        results = []
        rdict = {}
        for st in strs:
            s1 = list(st)
            s1.sort()
            s1 = "".join(s1)
            if s1 in rdict:
                rdict[s1].append(st)
            else:
                rdict[s1] = [st]
        return list(rdict.values())
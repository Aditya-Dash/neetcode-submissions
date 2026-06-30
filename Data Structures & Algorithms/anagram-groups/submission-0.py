class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.groupAnagramsSolutions(strs)
    
    def groupAnagramsSolutions(self, strs: List[str]) -> List[List[str]]:
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
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1= list(s)
        s1.sort()
        t1= list(t)
        t1.sort()
        return s1 == t1
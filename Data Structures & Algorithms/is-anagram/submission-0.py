class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check num of char
        if len(s) != len(t):
            return False
        # make all char lower
        s = s.lower()
        t = t.lower()
        # map all char to count for s
        s_count = dict.fromkeys("abcdefghijklmnopqrstuvwxyz", 0)
        for i in range(len(s)):
            s_count[s[i]] += 1
        # map all char to count for t
        t_count = dict.fromkeys("abcdefghijklmnopqrstuvwxyz", 0)
        for i in range(len(t)):
            t_count[t[i]] += 1
    
        if s_count != t_count:
            return False   
        
        return True


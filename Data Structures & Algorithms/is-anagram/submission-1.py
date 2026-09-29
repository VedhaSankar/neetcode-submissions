class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        s_hm = {}
        t_hm = {}

        for i, j in zip(s, t):
            if i in s_hm:
                s_hm[i] = s_hm[i] + 1
            else:
                s_hm[i] = 1
            
            if j in t_hm:
                t_hm[j] = t_hm[j] + 1
            else:
                t_hm[j] = 1

        if s_hm == t_hm:
            return True
        else:
            return False
            

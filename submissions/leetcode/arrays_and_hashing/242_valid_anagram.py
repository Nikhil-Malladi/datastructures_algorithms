class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        t=list(t)
        
        for i in t:
            if i not in s:
                return False
            s.remove(i)
        if len(s):
            return False
        return True

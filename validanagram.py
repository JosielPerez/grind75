class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sorted_s = [s[i] for i in range(0,len(s))]
        sorted_s.sort()

        sorted_t = [t[i] for i in range(0,len(t))]
        sorted_t.sort()

        if(sorted_s == sorted_t):
            return True
        else:
            return False
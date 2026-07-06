class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        for i in len(s):
          for j in range(len(s-1,-1,-1)):
                if s[i]==s[j]:
                    return True 
                else:
                    return False



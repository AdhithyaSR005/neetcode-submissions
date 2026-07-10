class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=sorted(s1)
        b=sorted(s2)
        n=len(s1)



        for x in range(len(s2)-n+1):
            if sorted(s2[x:x+len(s1):1])==a:
                return True 
            
        return False
        
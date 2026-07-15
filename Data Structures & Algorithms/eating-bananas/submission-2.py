import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

            
        left=1
        right=max(piles)

        while(left<right):
            avg=(left+right)//2
            count=0
            for x in piles:
                count=count+math.ceil(x/avg)
            
            if count<=h:
                left=left
                right=avg
            else:
                left=avg+1
                right=right

        return left

            







        
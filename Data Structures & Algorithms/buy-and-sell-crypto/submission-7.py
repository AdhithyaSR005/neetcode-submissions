class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min=0

        for x in range(len(prices)):
            for y in range(x+1,len(prices),1):
                if prices[y]-prices[x]>min:
                    min=prices[y]-prices[x]
                    y+=1
        return min 
                

        

    

            

        
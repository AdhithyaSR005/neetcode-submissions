class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=[]
        

        for x in range(len(heights)):

            
            
            for y in range(x+1,len(heights)):
                if heights[y]>heights[x]:
                    prod=heights[x]*len(heights[x:y])
                    res.append(prod)
                elif heights[y]<heights[x]:
                    prod=heights[y]*len(heights[x:y])
                    res.append(prod)
                elif heights[y]==heights[x]:
                    prod=heights[y]*len(heights[x:y])
                    res.append(prod)
                    

        return max(res)



                
                


            

        
class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[]
        rightmax=[]
        minus=[]

        for x in range(len(height)):
            leftmax.append(max(height[:x+1]))

        for y in range(len(height)):
            rightmax.append(max(height[y:]))

        for i in range(len(height)):
            a= min(leftmax[i],rightmax[i])-height[i]
            if a>=0:
                minus.append(a)
            else:
                minus.append(0)

        return sum(minus)


        
        
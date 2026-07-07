class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]

    
        for i in range(len(nums)):
            prod=1
            prod2=1
            for j in range (i+1,len(nums),1):
                prod= prod*nums[j]
                j+=1
            
            for k in range (0,i):
                prod2= prod2*nums[k]
                k+=1
                    
            out.append(prod*prod2)
        return out

                
                        


        
            
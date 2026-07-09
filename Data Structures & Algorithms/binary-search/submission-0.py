class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a=0
        b=len(nums)-1
       
        
        while a<=b:
            avg=int((a+b)/2)
            if nums[avg]==target:
                return avg
            elif nums[avg]<target :
                a=avg+1
            elif nums[avg]>target:
                b=avg-1
            
                
        return -1
        
        
        

        
        
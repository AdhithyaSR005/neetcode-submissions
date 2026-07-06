class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=len(nums)
        output=[]
        for i in range ( 0,a-1,1):
            for j in range(i+1,a,1):
                if nums[i]+nums[j]== target:
                    output.append(i)
                    output.append(j)
                    return output
        return output

        
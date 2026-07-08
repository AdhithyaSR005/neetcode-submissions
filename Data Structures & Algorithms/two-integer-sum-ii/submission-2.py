class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num=numbers
        output=[]
        for x in range(0,len(num),1):
            for j in range(x, len(num), 1):
                if num[x]+num[j]==target:
                    output.append(x+1)
                    output.append(j+1)
                    return sorted(output)
                
                    

        
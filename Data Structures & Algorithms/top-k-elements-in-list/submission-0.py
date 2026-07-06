class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output=[]
        a=[]
        seen = set()
        for i in nums:
            if i not in seen:
              a.append(nums.count(i))
              seen.add(i)
            else:
                continue
        order= sorted(a, reverse=True)
        for j in range (0,k,1):
            for l in nums:
                if nums.count(l)==order[j] and l not in output:
                    output.append(l)
                    break
        return output
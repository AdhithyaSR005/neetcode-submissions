class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        list=[0]
        
        for x in range(len(s)):
            vis=set()
            count=0
            if s[x] not in vis :
                count+=1
                vis.add(s[x])
                for y in range(x+1,len(s),1):
                    if s[y] not in vis :
                        count+=1
                        vis.add(s[y])
                    else:
                        break
                list.append(count)
        return max(list)
        

        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        visited = [False] * len(strs)

       
        for i in range(len(strs)):
            if visited[i]:
                continue
            a=[]
            my_string1 = strs[i]
            a.append(my_string1)
            visited[i] = True
            sorted_string1 = "".join(sorted(my_string1, key=str.lower))
            for j in range(i+1,len(strs),1):
                if visited[j]:
                    continue
                my_string2 = strs[j]
                sorted_string2 = "".join(sorted(my_string2, key=str.lower))
                if sorted_string1 == sorted_string2:
                    a.append(my_string2)
                    visited[j] = True
            output.append(a)
                    
        return output
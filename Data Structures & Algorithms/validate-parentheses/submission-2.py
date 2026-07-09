class Solution:
    def isValid(self, s: str) -> bool:
        brac={"]":"[",")":"(","}":"{"}
        stack=[]

        for x in s:
          if x in brac:
            if stack and stack[-1]==brac[x]:
              stack.pop()
            else:
              return False
          else:
            stack.append(x)
        return True if not stack else False
          

            




        
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num=[]
        op=['+','-','*','/']
        value=[]


        for x in range(len(tokens)):
            if tokens[x] not in op :
                num.append(tokens[x])
            
            elif tokens[x]=='+':
                a=int(num[-2])
                b=int(num[-1])
                num.pop()
                num.pop()
                val=a+b
                num.append(val)
            elif tokens[x]=='-':
                a=int(num[-2])
                b=int(num[-1])
                num.pop()
                num.pop()
                val=a-b
                num.append(val)
                
                

            elif tokens[x]=='*':
                a=int(num[-2])
                b=int(num[-1])
                num.pop()
                num.pop()
                val=a*b
                num.append(val)

            elif tokens[x]=='/':
                a=int(num[-2])
                b=int(num[-1])
                num.pop()
                num.pop()
                val=a/b
                num.append(val)

        return int(num[-1])

        
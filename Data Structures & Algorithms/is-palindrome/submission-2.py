class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for x in s:
            if x.isalnum():
                a+=x
        b=a.lower().replace(" ", "").replace("?","")
        if b[::1]==b[::-1]:
            return True 
        else:
            return False

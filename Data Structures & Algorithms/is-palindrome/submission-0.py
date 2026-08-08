class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if ord('a')<=ord(i)<=ord('z'):
                l.append(i)
            elif ord('A')<=ord(i)<=ord('Z'):
                l.append(i.lower())
            elif ord('0')<=ord(i)<=ord('9'):
                l.append(i)
            else:
                continue
        j=0
        for i in l[::-1]:
            if l[j]==i:
                l.pop(0)
            else:
                return False
        if l:
            return False
        else:
            return True

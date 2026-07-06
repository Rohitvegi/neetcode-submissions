class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        for i in s:
            if i in d1.keys():
                d1[i]+=1
            else:
                d1[i]=1
        for i in t:
            if i in d1.keys():
                if d1[i]!= 1:
                    d1[i]-=1
                else:
                    del d1[i]
            else:
                return False
        return not d1
        
        
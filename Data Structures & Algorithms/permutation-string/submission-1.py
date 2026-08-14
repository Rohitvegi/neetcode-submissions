class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1=Counter(s1)
        n=len(s1)
        l,u=0,n-1
        while u < len(s2):
            p=Counter(s2[l:u+1])
            if f1==p:
                return True
            else:
                l=l+1
                u=u+1
        return False




        
        




        
        
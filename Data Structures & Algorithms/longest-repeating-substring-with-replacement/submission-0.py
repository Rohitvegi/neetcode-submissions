class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,f,ans=0,0,0
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
            
            f=max(list(d.values()))
            while (((i-l+1)-f)>k):
                d[s[l]]=d.get(s[l])-1
                l=l+1
            ans=max(i-l+1,ans)
        return ans

            
                


            
    



            

        
class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            k=len(i)
            res=res+str(k)+'#'+i
        return res


    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i < len(s):
            k=i
            while s[k]!='#':
                k+=1
                
            n=int(s[i:k])
            l.append(s[k+1:k+1+n])
            i=k+1+n
        return l

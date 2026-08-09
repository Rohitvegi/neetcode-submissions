class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lu=sorted(nums)
        res=[]
        d={}
        for i in range(len(lu)):
            val=lu[i]
            l,u=i+1,len(nums)-1
            tar=-1*val
            while l<u:
                su=lu[l]+lu[u]
                if su>tar:
                    u=u-1
                elif su<tar:
                    l=l+1
                elif su == tar:
                    x="".join(map(str,sorted([val,lu[l],lu[u]])))
                    if x in d:
                        l=l+1
                        u=u-1
                        continue
                    else:
                        res.append([val,lu[l],lu[u]])
                        d[x]=1
                        l=l+1
                        u=u-1


        return res
                    


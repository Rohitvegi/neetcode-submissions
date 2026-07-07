class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        p=[]
        freq=[[]for i in range(len(nums)+1)]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,c in d.items():
            freq[c].append(i)
        for i in range(len(freq)-1,0,-1):
            if freq[i]:
                p.extend(freq[i])
            if len(p)==k:
                return p




        
        
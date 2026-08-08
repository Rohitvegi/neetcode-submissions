class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max=0
        s=set(nums)
        for i in nums:
            if (i-1) not in s:
                curr=i
                l=1
                while (curr+1) in s:
                    l+=1
                    curr=curr+1
                if max< l:
                    max=l
        return max


            

            






        
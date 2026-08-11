class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,u=0,0
        s1=set()
        maxl=0
        while u<len(s):
            if s[u] in s1:
                while s[u] in s1:
                    s1.remove(s[l])
                    l=l+1
            else:
                s1.add(s[u])
                maxl=max(maxl,u-l+1)
                u=u+1
        return maxl



      
            
        
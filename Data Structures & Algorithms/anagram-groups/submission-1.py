class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d={}
        for i in strs:
            c=[0]*26

            for j in i:
                c[ord(j)-ord('a')]+=1
            if tuple(c) in d.keys():
                d[tuple(c)].append(i)
            else:
                d[tuple(c)]=[i]
        return list(d.values())
        

        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        l,u=0,len(heights)-1
        while l<u:
            h=min(heights[l],heights[u])
            b=u-l
            a=h*b
            if heights[l]>heights[u]:
                u=u-1
            else:
                l=l+1
            if max<a:
                max=h*b
        return max

        
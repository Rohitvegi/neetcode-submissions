class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        l,u=0,len(heights)-1
        while l<u:
            b=u-l
            
            if heights[l]>heights[u]:
                h=heights[u]
                u=u-1
            else:
                h=heights[l]
                l=l+1
            a=h*b
            if max<a:
                max=h*b
        return max

        
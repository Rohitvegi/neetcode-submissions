class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre,post,o=[nums[0]],[nums[-1]],[]#1,6
        for i in range(1,len(nums)):#1 to 3
            pre.append(pre[i-1]*nums[i])
        i=1
        for j in range(len(nums)-2,-1,-1):
            post.append(post[i-1]*nums[j])
            i+=1
        post=post[::-1]
        o.append(post[1])
        for i in range(1,len(nums)-1):
                o.append(pre[i-1]*post[i+1])
        o.append(pre[-2])
        return o



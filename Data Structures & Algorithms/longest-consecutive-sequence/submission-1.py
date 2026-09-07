class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        num = set(nums)
        sorted_nums=sorted(num)

        out=[]    
        count=1

        for i in range(0, len(sorted_nums)-1):
            if sorted_nums[i+1] -1 == sorted_nums[i]:
                count+=1
            else:
                out.append(count)  
                count=1
        
        out.append(count)
        return max(out)
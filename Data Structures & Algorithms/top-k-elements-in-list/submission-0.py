class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}
        out = []
        for i in nums:
            if i not in dic:
                dic[i]=1
            else: 
                dic[i]+=1    
                
        top_k = sorted(dic , key=dic.get , reverse=True)[:k]
        return top_k


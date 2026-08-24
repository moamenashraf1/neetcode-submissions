class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for i in strs:
            sorted_strs = "".join(sorted(i))

            if sorted_strs not in dic:
                dic[sorted_strs]=[]
                
            dic[sorted_strs].append(i)
        return list(dic.values())    
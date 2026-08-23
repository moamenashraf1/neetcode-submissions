class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        j=0
        if len(s) == len(t):
            for i in s:
                if i != t[j]:
                    return False
                else: 
                    j+=1    
        else:
             return False

        return True

                
        
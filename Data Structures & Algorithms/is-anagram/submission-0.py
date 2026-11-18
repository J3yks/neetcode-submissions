class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ms={}
        mt={}
        for i in s: 
            ms[i]= 1+ms.get(i,0)

        for j in t:
            mt[j]= 1+mt.get(j,0)
   

        if mt==ms:
            return True

        return False
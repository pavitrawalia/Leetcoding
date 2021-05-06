class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        result=0
        for i in s:
            if i=="(":
                depth+=1
            elif i==")":
                depth-=1
            if depth>result:
                result=depth
        return result
                
                
        

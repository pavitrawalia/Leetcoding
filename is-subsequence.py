class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        front1 ,front2 = 0, 0
        while front1 < len(s) and front2 < len(t):
            if s[front1]==t[front2]:
                front1+=1
                front2+=1
            else:
                front2+=1
        return front1==len(s)

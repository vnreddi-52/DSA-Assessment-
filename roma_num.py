class Solution:
    def romanToInt(self, s: str) -> int:
        data={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        tot=0
        for i in range(len(s)-1):
            curr=data[s[i]]
            next=data[s[i+1]]
            if curr<next:
                tot-=curr
            else:
                tot+=curr
        return tot+data[s[-1]]
class Solution:
    def reverseWords(self, s: str) -> str:

        s = ' '.join(s.split())

        s = s.split(" ")

        res = []
        for i in range(len(s)):

            res.append(s.pop())


        return " ".join(res)

        


# ---------------2nd aproach---------------

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
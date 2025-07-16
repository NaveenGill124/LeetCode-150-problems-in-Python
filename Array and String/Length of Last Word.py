class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        end = len(s) - 1

        while s[end] == " ":
            end = end -1
        
        start = end

        while end >= 0 and s[end] != " ":

            end = end - 1
        
        return start - end






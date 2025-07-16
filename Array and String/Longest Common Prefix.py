class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""

        sort_s = sorted(strs)

        left = sort_s[0]
        right = sort_s[-1]

        # After sorting, the first and last strings in the list will be the most different.
        # Therefore, the common prefix between these two strings is guaranteed to be 
        # the longest common prefix shared among all strings in the list.
        # This works because sorting arranges strings lexicographically, 
        # so any common prefix among all strings must also be a prefix of the first and last.
        
        for i in range(min(len(left), len(right))): # this is like min of anyone left or right

            if left[i] != right[i]:
                return res
            
            res += left[i]

        
        return res
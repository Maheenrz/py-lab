class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix=strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix            



# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))     #
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length=0
        cleaned=s.strip()

        for i in cleaned[::-1]:
            if i == " ":
                break
            length+=1
        return length                




        
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = s.split()
        word.reverse()
        return " ".join(word)

        

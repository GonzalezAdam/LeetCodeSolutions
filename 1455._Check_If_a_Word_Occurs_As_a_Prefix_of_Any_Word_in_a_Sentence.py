class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        new = sentence.split()
        for word in new:
            if word.startswith(searchWord) == True:
                return new.index(word)+1
        return -1

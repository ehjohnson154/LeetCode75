

##You are given two strings word1 and word2.
#  Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        len1, len2 = len(word1), len(word2)

        while i < len1 or i < len2:
            if i < len1:
                merged.append(word1[i])
            if i < len2:
                merged.append(word2[i])
            i += 1

        return "".join(merged)


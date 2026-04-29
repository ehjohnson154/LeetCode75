
'''
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        #all about the length of str.
        larger string must be divisible by substring
        if not, we iterate into increasingly smaller substring

        To find GCD, we must account for three things
        -Are string lengths divisible by substring length?
        -Is substring repeatable through strings?
        
        To find these, we set up a iterator to check each substring of the smallest string (and thus largest GCD)
        And check each substring for these two conditions.
        If both equal, it repeats through whole string. Returning first instance of this returns our GCD
        If not found, return empty string. 
        '''
        #finding GCD between equal or smaller strings
   
        len1, len2 = len(str1), len(str2)
        largestGCD = min(len1, len2)

        if len1 == largestGCD:
            smallstr = str1
            largestr = str2
        else:
            smallstr = str2
            largestr = str1
   
        for i in range(largestGCD, 0, -1):
            if self.check_divisibility(smallstr, largestr, i):
                    if self.check_repeatability(smallstr, largestr, i):
                        return smallstr[:i]

        return ("")


    def check_divisibility(self, smallstr: str, largestr: str, i: int) -> bool:
            #Helper function to check if divisible
            if ((len(largestr) % len(smallstr[:i])) == 0 and (len(smallstr) % len(smallstr[:i]) == 0)):
                return True
            else:
                return False
            
    def check_repeatability(self, smallstr: str, largestr: str, i: int) -> bool:
        #Helper function to check if repeatable
        #Checks To confirm if the substring repeats through both itself and the larger/equal string
        size = len(largestr) // len(smallstr[:i])
        size2 = len(smallstr) // len(smallstr[:i])
        print(size)  
        if (smallstr[:i] * size == largestr) and (smallstr[:i] * size2 == smallstr):
            return True
        else:
                return False
        
        
'''      #Doesn't work due in large, complex patterns  
    def check_repeatability_old(self, smallstr: str, largestr: str, i: int, gcd: int) -> bool:

        #Doesn't work in large strings, since it might find a false positive
        if (smallstr[:i] == largestr[:i]) and (smallstr[:i] == largestr[-i:]):
            return True
        else:
             return False'''    
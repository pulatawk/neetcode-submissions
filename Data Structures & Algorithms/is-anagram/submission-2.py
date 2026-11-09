class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #sort the words -- same letters together 
        #compare total length of the word
        #compare if they have the same sorted 
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if len(s) == len(t):
            if sorted_s == sorted_t:
                return True

        return False
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a new list every time it is a different set of characters
        group_dict = defaultdict(list)

        #every word make them back into a string 
        for word in strs:
            sorted_word = "".join(sorted(word))
            group_dict[sorted_word].append(word)
        result = list(group_dict.values())
        return result
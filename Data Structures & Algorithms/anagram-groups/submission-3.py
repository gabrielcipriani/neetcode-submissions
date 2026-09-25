class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            count = [0]*26
            for letter in string:
                count[ord(letter) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(string)
        return list(anagrams.values())

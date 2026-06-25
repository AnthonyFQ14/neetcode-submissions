class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = defaultdict(list)

        for string in strs:
            d2 = tuple(sorted(string))
            d[d2].append(string)
        
        return list(d.values())
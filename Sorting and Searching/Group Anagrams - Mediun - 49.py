from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets_dict = dict()
        for s in strs:
            ss = "".join(sorted(s))
            if ss in sets_dict:
                sets_dict[ss].append(s)
            else:
                sets_dict[ss] = [s]

        return list(sets_dict.values())


solver = Solution()
print(solver.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(solver.groupAnagrams(["ddddddddddg","dgggggggggg"]))
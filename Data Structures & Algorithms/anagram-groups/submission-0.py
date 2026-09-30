class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sort = "".join(sorted(s))
            if sort in res:
                res[sort].append(s)
            else:
                res[sort] = [s]
        return list(res.values())
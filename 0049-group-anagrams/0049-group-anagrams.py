class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        if len(strs) == 0:
            return [""]
        wmap = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in wmap.keys():
                wmap[key].append(i)
            else:
                wmap[key] = [i]
        for k, v in wmap.items():
            out.append(v)
        return out 
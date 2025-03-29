class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        smap = {}
        for i in strs:
            k = ''.join(sorted(i))
            if k in smap.keys():
                smap[k].append(i)
            else:
                smap[k] = [i]
        for k, v in smap.items():
            out.append(v)
        return out
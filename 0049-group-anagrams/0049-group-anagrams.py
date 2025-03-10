class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        if len(strs) == 0:
            return output.append([""])
        
        wmap = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key in wmap.keys():
                wmap[key].append(i)
            else:
                wmap[key] = [i]

        for k in wmap.keys():
            output.append(wmap[k])
        return output
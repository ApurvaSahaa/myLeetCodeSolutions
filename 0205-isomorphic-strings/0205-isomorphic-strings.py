class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapdict = {}
        mapset = set(t)
        sp = tp = 0
        while sp < len(s) and tp < len(t) and len(mapset) > 0:
            if s[sp] in mapdict.keys():
                sp += 1
                tp += 1
            elif s[sp] not in mapdict.keys() and t[tp] in mapset:
                mapdict[s[sp]] = t[tp]
                mapset.remove(t[tp])
                sp += 1
                tp += 1
            else:
                sp += 1
                tp += 1
        res = ''.join(mapdict.get(c) for c in s if c in mapdict.keys())
        return res == t
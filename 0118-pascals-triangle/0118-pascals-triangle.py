class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1], [1, 1]]

        if numRows == 1:
            return [l[0]]
        if numRows == 2:
            return l
        for i in range(2, numRows):
            tmp = [1]
            seed = l[-1]
            for j in range(1, len(seed)):
                num = seed[j] + seed[j - 1]
                tmp.append(num)
            tmp.append(1)
            l.append(tmp)
        return l
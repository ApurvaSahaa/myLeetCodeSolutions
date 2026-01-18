class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                senior += 1
        return senior
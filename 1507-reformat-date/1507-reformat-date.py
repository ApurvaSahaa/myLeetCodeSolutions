class Solution:
    def reformatDate(self, date: str) -> str:
        # all dates are valid
        # so we can split the given date wrt the space character and get a list
        # for the year we have the last element
        # month is in a set which is unordered so we can try to get a list with the months
        # the same goes for day but we can just pick it up from the element
        # all the numeric elements of the day
        # for months we can just create a dict --> hardcoded
        
        
        year_dict = {
            'Jan' : 1,
            'Feb' : 2,
            'Mar' : 3,
            'Apr' : 4,
            'May' : 5,
            'Jun' : 6,
            'Jul' : 7,
            'Aug' : 8,
            'Sep' : 9,
            'Oct' : 10,
            'Nov' : 11,
            'Dec' : 12,
        }
        
        # list of date elements
        l = date.split()
        
        year = l[2]
        month = year_dict[l[1]]
        day = int(l[0][:-2])
        
        return f'{year}-{month:02d}-{day:02d}'
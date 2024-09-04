class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # create a dict 
        # have the id as the key and the scores as a list of 5 values
        # check if the size of list is 5 or less then 
        
        d = {}
        
        for i in items:
            if i[0] not in d:
                d[i[0]] = [i[1]]
            elif i[0] in d:
                d[i[0]].append(i[1])
        # now we have a dictionary with all the ids as key and a list of their scores as values
        
        # lets just try to go over the dictionary and create a list of list
        # add a list object with id and their average score to the list
        # we will sort the list and take top 5 scores with slicing if len greater than 5 or just sum
        # if len less or equal to 5
        
        res = []
        for key, value in d.items():
            value.sort()
            total = 0
            if len(value) > 5:
                for i in value[-5:]:
                    total += i
                res.append([key, total//5])
            else:
                for i in value:
                    total += i
                res.append([key, total//5])
        
        res.sort()
        return res
class Solution:
    def minimumChairs(self, s: str) -> int:
        
        # s represents a valid sequence of entries and exits
        # meaning s cannot start with a L
        
        # have a min of 1 chair in the room
        # have zero people in the room
        chair_s = 1
        people = 0
        
        # loop over the string
        # if item is E compare the chairs and people entered
        # if chairs is less than people entered add a chair
        # if item is L decrement the number of people
        
        for i in s:
            if i == 'E':
                people += 1
                if chair_s < people:
                    chair_s += 1
            else:
                people -= 1
                
        return chair_s
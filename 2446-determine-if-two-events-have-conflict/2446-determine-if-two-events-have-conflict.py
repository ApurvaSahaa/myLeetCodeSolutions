class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return event1[0] <= event2[1] and event2[0] <= event1[1]
    
    # event 1 must start before event 2 ends
    # event 2 must start before event 1 ends
    
    # for no conflict
    # event 1 must start before event 2 ends
    # event 2 must start after event 1 ends
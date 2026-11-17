"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        si = sorted(intervals, key=lambda i: i.start) # sort by start time

        max_rooms = 0
        room_list: list[int] = []
        for i in si:
            # check if we have a room booked already
            if len(room_list) == 0:
                # if not, add this to the room list
                heapq.heappush(room_list, i.end)
            else:
                # if we do, check the end time
                if room_list[0] <= i.start:
                    # if end < start : replace the heap with
                    heapq.heapreplace(room_list, i.end)
                else:
                    # else push onto the heap
                    heapq.heappush(room_list, i.end)

            #increment max roomcount == size heapq
            max_rooms = max(max_rooms, len(room_list))

        return max_rooms


'''
QUESTION -
----------
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
Example:
Input: [[15, 20],[5, 10],[0, 30]]
Output: 2

APPROACH -
----------
Using Min Heap:

    Edge Case -
        1. If the list of intervals is empty, then return 0

    1. Sort the given array of start, end times by increasing order of start time.
    2. Initialize the count of meeting rooms to 1.
    3. Push the end time of the interval at index = 0 to the heap.
    4. Iterate through the list of time intervals starting from index = 1:
        - if the start time < root of current min heap:
            - increment the counter of meeting rooms
            - push the end time of that time interval to the heap.
        - if the start time > root of current min heap:
            - simply push the end time of that time interval to the heap and pop the root element of min heap.
    5. Return the count of meeting rooms

    Time Complexity -
    -----------------
    - Sorting of N elements: O(NlogN)
    - Pushing and Popping of elements to/from heap: O(logN)
    - In worst case, all meetings will clash and we will have to do push and pop operation for all N intervals in the list. Then time complexity will be O(NlogN)

    Space Complexity -
    ------------------
    - O(N) as we created a min heap. In worst case, the min heap can contain all the N elements.

Iterative Method:
    Edge Case -
        1. If the list of intervals is empty, then return 0

    1. Seperate the start and end times from the intervals list.
    2. Sort them seperately.
    3. Initialize the count of meeting rooms booked to 0.
    4. Consider iteration pointers i and j for start_times and end_times respectively.
    5. Keeping the pointer of end_times at the start position, iterate through the start_times list.
        - If the start time is less than the end time corresponding to the pointer, that means a new meeting room should be booked as there is no empty room.
        - If the start time is greater than the end time corresponding to the pointer, that means the previous meeting is over or going to be over soon. So the new meeting can happen in the same meeting room. No need to book different room. Also increment the end_times pointer.

    Time Complexity -
    -----------------
    - Sorting of start and end times - O(NlogN)
    - Iterating through the start time list - O(N)
    - Overall: O(NlogN) + O(N) ~ O(NlogN)

    Space Complexity -
    ------------------
    O(N) as we created 2 sorted lists.

'''

import heapq as hq


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        # Sorting the list of intervals in the ascending order of start times. Sorting takes O(logN) time and as this needs to be done for N elements, time complexity is O(NlogN)
        sorted_intervals = sorted(intervals)
        heap = []
        count = 1
        hq.heappush(heap,sorted_intervals[0][1]) # Pushing the end time of 1st interval to the heap.

        for i in range(1,len(sorted_intervals)):
            if sorted_intervals[i][0] < heap[0]: # If start time of the interval < end time of previous interval.
                count += 1
                hq.heappush(heap,sorted_intervals[i][1]) # Pushing the end time of the current interval to the heap. After pushing a element, maintaining the min heap property takes O(logN) time.
            else:
                hq.heappushpop(heap,sorted_intervals[i][1]) # Pushing and popping takes O(logN) time to maintain the min heap property afterwards.

        return count

    def minMeetingRoomsIterative(self,intervals):
        if not intervals:
            return 0

        start_times = []
        end_times = []
        # Iterating through intervals to seperate start and end times. This takes O(N) time.
        for i in range(len(intervals)):
            start_times.append(intervals[i][0])
            end_times.append(intervals[i][1])
        # Sorting both start and end times. This will take O(NlogN) time
        sorted_start = sorted(start_times)
        sorted_end = sorted(end_times)
        count = 0

        i = 0
        j = 0
        # Iterating through the start time list and comparing every start time with one end time in a single loop. This is done to check if a meeting is starting after completion of some other meeting, then the same meeting room can be booked.
        # This will take O(N) time.
        while i < len(sorted_start):
            if sorted_start[i] < sorted_end[j]:
                count += 1
                i += 1
            else:
                j += 1
                i += 1

        return count


if __name__ == '__main__':
    s = Solution()
    intervals = [[7,10],[2,4]]
    # print(s.minMeetingRooms(intervals))
    print(s.minMeetingRoomsIterative(intervals))

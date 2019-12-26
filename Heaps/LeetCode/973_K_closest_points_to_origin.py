'''
QUESTION -
----------
https://leetcode.com/problems/k-closest-points-to-origin/
Given - List of points
Find K closest points to the origin(0,0)

Example:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.

APPROACH -
----------
By building a min heap:
    1. As we have to find the closest points to the origin, we will have to calculate the distance of each point given in the input from the origin.
    2. Define a helper function which will take 2 points (origin and other point) and return the distance between them.
    3. Create a result list consisting of tuples in the form: (distance,(coordinates)) which tells us the distance of the coordinates from (0,0)
    4. Convert the result list into a min heap.
    5. Return first K coordinates from the heap.

TIME COMPLEXITY -
-----------------
For given N points and to find K closest points:
    - Finding distance of each point in the input list from origin - O(N)
    - Performing heapq.nsmallest(K, list) to find K nearest points to the origin - O(N*logK)
    - Iterating over K dist,points tuples to append only point to the result list - O(K)

If N is very large compared to K, then time complexity - O(N) + O(N*logK)
Note - if K is very small compared to N, then amortized time can be written as O(N)

SPACE COMPLEXITY -
------------------
As we created a list to store distance and points, it will take O(N) time.
'''

import heapq as hq
import math



class Solution:
    def kClosest(self, points, K):
        # Finding distance of the given point from origin(0,0).
        def findDistance(point):
            x = point[0]
            y = point[1]
            dist = math.sqrt((x)**2 + (y)**2)

            return dist

        dist_list = [] # [(dist,[x,y])]
        result = [] # List of K points near to origin.

        # Going through each point to find the distance of point from the origin. It takes O(N) time.
        for point in points:
            dist_list.append(((findDistance(point)), point))

        # heapifying the distance - point list as min heap. It takes O(N) time.
        hq.heapify(dist_list)
        k_closest = hq.nsmallest(K,dist_list) # Finding K smallest elements from list of N elements takes O(Nlog(K)) time.

        for dist,point in k_closest: # This will take O(K) time
            result.append(point)

        return result

if __name__ == '__main__':
    s = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    print(s.kClosest(points,K))

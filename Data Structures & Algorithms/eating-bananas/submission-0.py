from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def finish(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
            return hours

        left = 1 
        right = max(piles)
        answer = max(piles)

        while left <= right:
            mid = (right + left)//2

            hours = finish(mid)

            if hours <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
    


        
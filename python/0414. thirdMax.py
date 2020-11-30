class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        hq = []
        for x in nums:
            if x not in hq:
                if len(hq) < 3:
                    heapq.heappush(hq, x)
                else:
                    heapq.heappushpop(hq, x)
        if len(hq) < 3:
            return hq[-1]
        return hq[0]

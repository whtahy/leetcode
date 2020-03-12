# pairwise slopes
class Solution:
    def slope(a, b):
        delta_y = abs(a[1]-b[1])
        delta_x = abs(a[0]-b[0])
        if delta_x == 0:
            return math.inf
        else:
            return delta_y / delta_x

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        if n == 2:
            return True

        m = Solution.slope(coordinates[0], coordinates[-1])
        return all(m == Solution.slope(coordinates[i], coordinates[i+1]) for i in range(0, n-1, 2))

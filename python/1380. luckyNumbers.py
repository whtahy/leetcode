class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        m_min = [math.inf] * m
        n_max = [0] * n

        for row in range(m):
            for col in range(n):
                x = matrix[row][col]
                if x < m_min[row]:
                    m_min[row] = x
                if x > n_max[col]:
                    n_max[col] = x

        return [x for x in set(m_min) & set(n_max)]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            if i == 0:
                triangle.append([1])
                continue
            elif i == 1:
                triangle.append([1, 1])
                continue

            row = []
            for j in range(i-1):
                sum = triangle[-1][j] + triangle[-1][j+1]
                row.append(sum)

            triangle.append([1] + row + [1])

        return triangle

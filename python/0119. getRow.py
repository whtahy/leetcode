class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex+1):
            if i == 0:
                triangle = [1]
                continue
            elif i == 1:
                triangle = [1, 1]
                continue

            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = triangle[j] + triangle[j-1]

            triangle = row

        return triangle

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [
            [1],
            [1,1]
        ]

        if rowIndex == 0 or rowIndex == 1:
            return rows[rowIndex]
        
        def nextRow(previousRow: List[int]) -> List[int]:
            nextRow = [1]
            for i in range(0, len(previousRow) - 1):
                nextRow.append(previousRow[i] + previousRow[i+1])
            nextRow.append(1)
            print(nextRow)
            return nextRow

        for i in range(2, rowIndex + 1):
            rows.append(nextRow(rows[i-1]))

        return rows[rowIndex]
        
        
        
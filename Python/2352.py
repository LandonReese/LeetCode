# 2352. Equal Row and Column Pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # gridList: Create list of sequential numbers from the grid
        # subList:  Stores each row/column to then be added into gridList
        gridList = []
        subList = []

        # Return number
        final = 0 # Add 1 each time a matching set is found

        #Populate list both ways
        for i in range(0, len(grid)):
            for j in range(0, len(grid)):
                subList.append(grid[i][j])
            gridList.append(subList)
            subList = []

        #print(0, subList)
        #print(1, gridList)

        for j in range(0, len(grid)):
            for i in range(0, len(grid)):
                subList.append(grid[i][j])
            gridList.append(subList)
            subList = []

        #print(2, subList)
        #print(3, gridList)
        #print(len(gridList))
        #print(int(len(gridList)/2))

        # Take gridList and see if any of the first half lists is equal to the values of any of the second half lists
        for i in range(0, int(len(gridList)/2)):
            iComparator = gridList[i]
            for j in range(int(len(gridList)/2), len(gridList)):
                jComparator = gridList[j]
                #print("i", iComparator)
                #print("j", jComparator)
                if(iComparator == jComparator):
                    final += 1
        
        
        return final
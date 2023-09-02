from typing import List  # Import the List type hint

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        return_list = [[1]]
        
        for i in range(1, numRows):
            previous_row = return_list[-1]
            next_row = [1]
            
            for j in range(1, i):
                next_row.append(previous_row[j - 1] + previous_row[j])
        
            next_row.append(1)
            return_list.append(next_row)
        print(f"{return_list}")
            
        return return_list
            
def main():
    solution = Solution()
    test_variable = 5
    solution.generate(test_variable)

if __name__ == "__main__":
    main()
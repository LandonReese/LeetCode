from typing import List

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """_summary_

        Args:
            columnTitle (str): The column title, e.g. "A", "Z", "AB", "AAXBY" etc.

        Returns:
            int: The integer of the calculated column number
        """
        result = 0
        
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
            
        return result
            

def main():
    solution = Solution()
    test_variable1 = "Z"
    test_variable2 = "FXSHRXW"
    test_variable3 = "ZY"
    print(solution.titleToNumber(test_variable1))
    print(solution.titleToNumber(test_variable2))
    print(solution.titleToNumber(test_variable3))

if __name__ == "__main__":
    main()
    
    
    # sum = 0
    #    
    #     if len(columnTitle) == 1:
    #         return self.columnToLetter(columnTitle[0])
    #     value_list = []
    #     for i in range(0, len(columnTitle)):
    #         if i == len(columnTitle) - 1:
    #             value_list.append(self.columnToLetter(columnTitle[i]))  
    #         else:
    #             value_list.append(pow(26, (i+1)) + self.columnToLetter(columnTitle[i]))   
        
    #     sum = self.listToLetter(value_list)
        
    #     return sum
        
    # def columnToLetter(self, letter: str) -> int:
    #     alphabet = " ABCDEFGHIJKLMNOPQESTUVWXYZ"
    #     for i in range(1, len(alphabet)):
    #         if letter == alphabet[i]:
    #             return i
            
    # def listToLetter(self, list:List[int]) -> int:
    #     sum = 0
    #     print(f"List 1: {list}")
    #     for i in range(0, len(list)):
    #         if i == 0:
    #             sum = list[i]
            
    #         if i == len(list) - 1:
    #             sum += list[i]
    #         else:
    #             sum = 26 * list[i]
    #             list[i] = sum
                
    #     print(f"List 2: {list} {sum}")
    #     return sum
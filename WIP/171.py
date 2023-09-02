class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """_summary_

        Args:
            columnTitle (str): The column title, e.g. "A", "Z", "AB", "AAXBY" etc.

        Returns:
            int: The integer of the calculated column number
        """
        running_sum = 0
        
        for i in range(0, len(columnTitle)):
            running_sum += self.columnToLetter(columnTitle[i])
        
        print(f"running_sum {running_sum}")
        return running_sum
        
    def columnToLetter(self, letter: str) -> int:
        alphabet = " ABCDEFGHIJKLMNOPQESTUVWXYZ"
        for i in range(1, len(alphabet)):
            if letter == alphabet[i]:
                return i

def main():
    solution = Solution()
    test_variable = "AA"
    solution.titleToNumber(test_variable)

if __name__ == "__main__":
    main()
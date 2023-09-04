class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = self.digitAdder(num)
            
        return num
    
    def digitAdder(self, num: int) -> int:
        string_num = str(num)
        sum = 0
        for i in range(0, len(string_num)):
            sum += int(string_num[i])
            
        print(f"sum {sum}")
        return sum
    
    
    
def main():
    solution = Solution()
    test_variable = 69857469642
    solution.addDigits(test_variable)

if __name__ == "__main__":
    main()
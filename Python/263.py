class Solution:
    def isUgly(self, n: int) -> bool:
        condition = True
        if n == 0:
            return False
        while condition:
            if n % 2 == 0:
                n = n/2
            elif n % 3 == 0:
                n = n/3
            elif n % 5 == 0:
                n = n/5
            else:
                condition = False

            print(f"n {n}")
            
        if n > 5 or n < 0:
            return False
        return True
        
def main():
    solution = Solution()
    test_variable = -2147483648
    print(solution.isUgly(test_variable))

if __name__ == "__main__":
    main()
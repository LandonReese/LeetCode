class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        list_of_2s = []
        for i in range(0, 31):
            list_of_2s.append(pow(2, i))
        print(f"{list_of_2s}")    
        if n in list_of_2s:
            return True
        return False
        
            
def main():
    solution = Solution()
    test_variable = 64
    print(solution.isPowerOfTwo(test_variable))

if __name__ == "__main__":
    main()
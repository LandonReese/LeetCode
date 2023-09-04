class Solution:
    def hammingWeight(self, n: int) -> int:
        hex = hex(n)
        print(f"{hex}")
        

def main():
    solution = Solution()
    test_variable = 10001101000101001011011011111001
    solution.hammingWeight(test_variable)

if __name__ == "__main__":
    main()
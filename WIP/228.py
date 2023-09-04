from typing import List  # Import the List type hint

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        starting = nums[0]
        traversal = 0
        print(f"{starting}")
        
        
        for i in range(0, len(nums) - 1):
            current = nums[i + 1]
            print(f"{starting}")
            

def main():
    solution = Solution()
    test_variable = [1,2,3,4,5,6,7,8,9]
    print(solution.summaryRanges(test_variable))

if __name__ == "__main__":
    main()
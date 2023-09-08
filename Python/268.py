from typing import List  # Import the List type hint

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(f"nums {nums}")
        for i in range(0, len(nums)):
            print(nums[i])
            if nums[i] != i:
                print(f"Return {i}")
                return i
        print(f"Return {len(nums)}")   
        return len(nums)

def main():
    solution = Solution()
    test_variable = [9,6,4,2,3,5,7,0,1,8]
    solution.missingNumber(test_variable)

if __name__ == "__main__":
    main()
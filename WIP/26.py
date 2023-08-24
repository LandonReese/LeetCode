from typing import List  # Import the List type hint

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_numbers = {}
        for i in range(0, len(nums)):
            number_to_add = nums[i]

            if number_to_add not in unique_numbers:
                unique_numbers[number_to_add] = None
        nums = list(unique_numbers.keys())
        print(f"Unique Numbers | {len(list(unique_numbers.keys()))}")
        print(f"Nums | {nums}")
        return len(list(unique_numbers.keys()))
        
def main():
    solution = Solution()
    test_variable = [1, 1, 2]
    solution.removeDuplicates(test_variable)

if __name__ == "__main__":
    main()
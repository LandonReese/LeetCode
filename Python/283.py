from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(f"Start\n{nums}")
        num_zeros = 0
        num_list = []
        for i in range(0, len(nums)):
            
            if nums[i] == 0:
                num_zeros += 1
                
            else:
                num_list.append(nums[i])
                
        for i in range(0, len(num_list)):
            nums[i] = num_list[i]
                
        for i in range(len(nums) - num_zeros, len(nums)):
            nums[i] = 0
        
        print(f"\nFinal\n{nums}")
        
def main():
    solution = Solution()
    test_variable = [0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0]
    solution.moveZeroes(test_variable)

if __name__ == "__main__":
    main()
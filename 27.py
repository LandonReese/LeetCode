from typing import List  # Import the List type hint

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numbers_removed = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                numbers_removed = numbers_removed + 1
        
        
        return numbers_removed
    
    def sortFunction(self, nums: List[int]):
        print(f"Before Sort: {nums}")
        temp = ""
        for i in range(0, len(nums) - 1):
            if nums[i] == "_":
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
                
        print(f"After Sort: {nums}")
        
    def returnCount(self, nums: List[int]) -> int:
        num_count = 0
        for i in range(0, len(nums)):
            if nums[i] == "_":
                
            
            
        
def main():
    solution = Solution()
    test_list = [1, 1, 1, 1]
    test_int = 2
    # solution.removeElement(test_list, test_int)
    print(f"Removed {solution.removeElement(test_list, test_int)}")
    print(f"Final list: {test_list}")
    

if __name__ == "__main__":
    main()
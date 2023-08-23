from typing import List  # Import the List type hint

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numbers_removed = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                nums[i] = "_"
                numbers_removed = numbers_removed + 1
        
        
        return self.sortAndReturnCount(nums)
    
    def sortAndReturnCount(self, nums: List[int]) -> int:
        print(f"Before Sort: {nums}")
        num_count = 0
        amount_to_append = 0
        list_of_numbers = []
        for item in nums:
            if item != "_":
                list_of_numbers.append(item)
                num_count = num_count + 1
            else:
                amount_to_append = amount_to_append + 1

        for i in range(0, amount_to_append):
            list_of_numbers.append("_")

        for i in range(0, len(list_of_numbers)):
            nums[i] = list_of_numbers[i]
                
        print(f"After Sort: {nums}")
        return num_count
                
            
            
        
def main():
    solution = Solution()
    test_list = [2, 1, 2, 2, 4, 6, 7, 3, 2, 8, 2, 2, 2, 2, 2, 2, 7, 8, 9, 100, 2]
    test_int = 2
    # solution.removeElement(test_list, test_int)
    print(f"# of Elements {solution.removeElement(test_list, test_int)}")
    print(f"Final list: {test_list}")
    

if __name__ == "__main__":
    main()
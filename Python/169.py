from typing import List  # Import the List type hint

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_num_dict = {}
        majority_value = 0
        for i in range(0, len(nums)):
            if nums[i] not in unique_num_dict:
                unique_num_dict[nums[i]] = 1
                
            else:
                unique_num_dict[nums[i]] += 1
                
        print(f"Dict: {unique_num_dict}")
        
        for item in unique_num_dict:
            # print("Key:", item)
            # print("Value:", unique_num_dict[item])
            if unique_num_dict[item] > majority_value:
                majority_value = unique_num_dict[item]
                majority_key = item
        
        print(f"Returning: {majority_key}")
        print(f"Occurs: {majority_value}")
        return majority_key    

def main():
    solution = Solution()
    test_variable = [3,2,3]
    solution.majorityElement(test_variable)

if __name__ == "__main__":
    main()

from typing import List  # Import the List type hint
import sys

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        number_dict = {}
        number_key = -1
        number_value = sys.maxsize
        smallest_even_val = -1
        
        for i in range(0, len(nums)):
            if nums[i] not in number_dict:
                number_dict[nums[i]] = 1
                
            else:
                number_dict[nums[i]] += 1
                
        for key in number_dict:
            print(f"key {key}")
            if number_dict[key] < number_value and key % 2 == 0:
                # smallest_even_val = number_dict[key]
                print(f"1: n_d[k] | {number_dict[key]}")
                
                if number_value == -1:
                    number_value = number_dict[key]
                    number_key = key
                
                else:
                    if number_dict[key] < number_value:
                        number_value = number_dict[key]
                        number_key = key
        
        print(f"\nKey {number_key}")
        print(f"Val {number_value}")
                
        print(f"\nnumber_dict")
        print(f"{number_dict}")
            
        print(f"{number_key}")
        return number_key 

def main():
    solution = Solution()
    test_variable = [8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]
    solution.mostFrequentEven(test_variable)

if __name__ == "__main__":
    main()

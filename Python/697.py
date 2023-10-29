from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        number_dict = {}
        highest_frequency = 0
        
        for num in nums:
            if num not in number_dict:
                number_dict[num] = 1
            else:
                number_dict[num] += 1
                
        # print(f"nums: {nums} \n n_dict: {number_dict}")
        
        for item in number_dict:
            print(f"item: {item} | nd[item] {number_dict[item]}")
            if number_dict[item] > highest_frequency:
                print(f"HF: {highest_frequency}")
                highest_frequency = item
                
        return highest_frequency

def main():
    solution = Solution()
    test_variable = [1, 2, 3, 4, 5, 7, 12, 18, 1, 1, 1, 1, 1, 4]
    answer = solution.findShortestSubArray(test_variable)
    print(answer)
    

if __name__ == "__main__":
    main()
    
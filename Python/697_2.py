# Constraints:

# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.


from typing import List

class Solution: 
    class Number:
        num = -1
        start_index = -1
        end_index = -1
        occurrences = 0
        
    def findShortestSubArray(self, nums: List[int]) -> int:
        """Create a subarray, and return the shortest subarray of the highest degree

        Args:
            nums (List[int]): List of occurring numbers

        Returns:
            int: The length of the shortest subarray of the integers of the highest frequency
        """
        # Same thing but with classes
        number_dict = {}
        number_list = []
        max_occurrences = 0
        
        for i in range(0, len(nums)):
            if nums[i] not in number_dict:
                number_dict[nums[i]] = 1
            else:
                number_dict[nums[i]] += 1
                
        print(number_dict)
        
        for n in number_dict:
            number = self.Number()
            number.num = n
            number.occurrences = number_dict[n]
            number_list.append(number)

        for i in range(0, len(nums)):
            for n in number_list:
                if n.num == nums[i]:
                    print(f"{n.num} {n.occurrences} {n.start_index}")
                    if n.start_index == -1:
                        n.start_index = i
                    n.end_index = i
                    if n.occurrences > max_occurrences:
                        max_occurrences = n.occurrences
            
        # number = self.Number()
        # number.num = nums[i]
        # number.start_index = i
        # number.end_index = i
        # number.occurrences += 1
        # number_list.append(number)
            
        smallest_subarray_length = len(nums)
        for n in number_list:
            print(f"\nnum:{n.num}\nocc:{n.occurrences}\nsi:{n.start_index}\nei:{n.end_index}\n")
            if (n.end_index - n.start_index) < smallest_subarray_length and n.occurrences == max_occurrences:
                smallest_subarray_length = (n.end_index - n.start_index) + 1
                
        return smallest_subarray_length
            
        
            
                    
def main():
    solution = Solution()
    test_variables = [
        [1,2,2,3,1], 
        [1,2,2,3,1,4,2],
        [98, 97, 96, 97, 99, 99]
    ]
    
    answers = [
        2,
        6,
        2,
    ]
    
    for i in range(0, len(test_variables)):
        print(f"Test number: {i + 1}\n")
        answer = solution.findShortestSubArray(test_variables[i])
        print("shortest subarry length is " + str(answer))
        assert answer == answers[i]
    

if __name__ == "__main__":
    main()
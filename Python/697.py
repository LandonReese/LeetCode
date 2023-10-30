from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """Create a subarray, and return the shortest subarray of the highest degree

        Args:
            nums (List[int]): List of occurring numbers

        Returns:
            int: The length of the shortest subarray of the integers of the highest frequency
        """
        number_dict = {}
        degree_num = -1
        
        # Fill number dictionary
        for i in range(0, len(nums)):
            # First occurrence, assign start
            if nums[i] not in number_dict:
                number_dict[nums[i]] = {}
                number_dict[nums[i]]["occurrences"] = 1
                number_dict[nums[i]]["start"] = i
                number_dict[nums[i]]["end"] = i
                
            
            # Alternative occurrences
            else:
                number_dict[nums[i]]["occurrences"] += 1
                number_dict[nums[i]]["end"] = i   
            
            # For each element, save the max degree
            if degree_num == -1 or number_dict[nums[i]]['occurrences'] > number_dict[degree_num]['occurrences']:
                degree_num = nums[i]
            
            else:
                if number_dict[nums[i]]['occurrences'] == number_dict[degree_num]['occurrences']:
                    if (number_dict[nums[i]]['end'] - number_dict[nums[i]]['start']) < (number_dict[degree_num]['end'] - number_dict[degree_num]['start']):
                        degree_num = nums[i]
            
            print(f"TEST: {i} oc:{number_dict[nums[i]]['occurrences']} de:{degree_num}")
                
        print(f"{number_dict} \n degree_num {degree_num} | degree of array: {number_dict[degree_num]['occurrences']}")
        
        return number_dict[degree_num]["end"] - number_dict[degree_num]["start"] + 1
        
            
                    
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
    
# number_dict = {}
# key = -1
# value = -1
# last_occurrence = -1

# subarray = []

# for num in nums:
#     if num not in number_dict:
#         number_dict[num] = 1
#     else:
#         number_dict[num] += 1

# # The error occurs in these lines
# for item in number_dict:
#     if number_dict[item] > value:
#         key = item
#         value = number_dict[item]

# for i in range(0, len(nums)):
#     if nums[i] == key:
#         for j in range(i, len(nums)):
#             subarray.append(nums[j])
#         break  

# for i in range(0, len(subarray)):
#     if subarray[i] == key:
#         last_occurrence = i  

# subarray = subarray[0:last_occurrence + 1]

# return len(subarray)
    
from typing import List  # Import the List type hint

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Add all lines here
        
        nums <-list
        for each number we encounter:
            if(list has number)
                list.pop(element 'number')
            else
                list.add(number)        
        """
        print(f"Nums: {nums}")
        number_list = []
        
        for i in range(0, len(nums)):
            if nums[i] not in number_list:
                number_list.append(nums[i])
            else:
                number_list.pop(number_list.index(nums[i]))

        print(number_list)         
        return number_list[0]
        
        # # If it is already in list   
        # if number_list.at(number) == True:
        #     number_list.pop(number)
            
        # if number not in number_list:
        #     number_list[number] = True
            
        # print(number_list)
        
    
def main():
    test_variable = [1, 2, 2, 4, 3, 3, 4]
    Solution().singleNumber(test_variable)

if __name__ == "__main__":
    main()
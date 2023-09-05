from typing import List  # Import the List type hint

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
       
        result = []
        start = nums[0]
        end = nums[0]
       
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                
                start = end = nums[i]
        
        if start == end:
            result.append(str(start))
            
        else:
            result.append(f"{start}->{end}")
            
        return result
            
             
            
            

def main():
    solution = Solution()
    test_variable = [0,1,3,5,6,7,8,9,11]
    print(solution.summaryRanges(test_variable))

if __name__ == "__main__":
    main()
    
    #  current = True
    #     print_string = ""
    #     print_list = []
    #     if len(nums) == 1:
    #         return [str(nums[0])]
        
    #     for i in range(0, len(nums) - 1):
    #         # print(f"{len(nums) - 1} {len(nums)}")
    #         if current:
    #             print_string += str(nums[i]) 
    #             current = False
    #         print(f"print1 {print_string}")
    #         if nums[i + 1] == nums[i] + 1:
    #             if i + 1 == len(nums) - 1 and nums[i + 1] == nums[i] + 1:
    #                 print(f"bbbbb")
    #                 print_string += "->"
    #                 print_string + str(nums[i + 1])
    #                 print_list.append(print_string)
    #                 print_string = ""
    #                 current = True
    #                 break
    #             i += 1
    #             continue
    #         else:
    #             print_string += "->"
    #             print_string += str(nums[i])
    #             print(f"print2 {print_string}")
    #             print_list.append(print_string)
    #             print_string = ""
    #             current = True
    #     # if nums[len(nums) - 1] != nums[len(nums) - 2] + 1:
    #     #     print_list.append(str(nums[len(nums)]))
               
    #     print(f"print_list {print_list}")
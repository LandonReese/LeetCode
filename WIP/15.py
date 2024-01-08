from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if i == j or i == k or j == k:
                        continue
                    else:
                        if nums[i] + nums[j] + nums[k] == 0:
                            return_list.append([nums[i], nums[j], nums[k]])
                            #print(return_list)
        
         
        for i in range(0, len(return_list)):
            return_list[i] = sorted(return_list[i])   
          
        
        unique_list = []  
        for i in range(0, len(return_list)):
            if return_list[i] not in unique_list:
                unique_list.append(return_list[i])
                    
        return unique_list
                        
        
def main():
    inputs = [
        [-1,0,1,2,-1,-4],
        [0,1,1],
        [0,0,0],
    ]
    
    outputs = [
        [[-1,0,1],[-1,-1,2]],
        [],
        [[0,0,0]],
    ]
    
    s= Solution()
    
    for i in range(0, len(inputs)):
        assert(s.threeSum(inputs[i]) == outputs[i])
    
if __name__ == "__main__":
    main()
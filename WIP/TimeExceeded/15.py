from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        n = len(nums)
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        ret = sorted([nums[i], nums[j], nums[k]])
                        if ret not in return_list:
                            return_list.append(ret)

        print(return_list)
                    
        return return_list
                        
        
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
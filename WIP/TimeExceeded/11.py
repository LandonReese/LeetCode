from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        switchJ = True

        for i in range(0, len(height)):
            
            
            for j in range(len(height) - 1, i, -1):
                
                b = j - i
                if height[i] < height[j]:
                    h = height[i]
                else:
                    h = height[j]
                
                if b * h > volume:
                    volume = b * h
                    
        return volume
        
def main():
    inputs = [
        [1,8,6,2,5,4,8,3,7],
        [1,1],
        [0,0,0,0,0,0,0,0,0],
        [0,1,2,3,4,5,6,7,8],
        [0,1,2,3,4,3,2,1,0],
        
    ]
    
    outputs = [
        49,
        1,
        0,
        16,
        8,
    ]
    
    s = Solution()
    
    for i in range(0, len(inputs)):
        print(i, "Passed.")
        assert(s.maxArea(inputs[i]) == outputs[i])
    
if __name__ == "__main__":
    main()
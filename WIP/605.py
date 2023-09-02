from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """ Returns true if the amount of flowers can fit in the flowerbed

        Args:
            flowerbed (List[int]): The list containing the flower locations (1) 
            and empty pots (0)
            n (int): how many flowers to plant

        Returns:
            bool: True if the amount of plants can be planted, false otherwise
        """
        print(f"flowerbed {flowerbed}")
        test_list = self.fillTestArray(flowerbed)
        print(f"flowerbed {flowerbed}")
        count_added = 0
        
        print(f"flowerbed {flowerbed}")
        print(f"test_list {test_list}")
        
        for i in range(0, len(test_list)):
            if flowerbed[i] != test_list[i]:
                count_added += 1
                
        if count_added >= n:
            return True
        
        return False
    
    def isValidFlowerSpot(self, flowerbed: List[int], index: int):
        if len(flowerbed) == 0:
            return -1
        
        if len(flowerbed) == 1:
            return not flowerbed[0]
        
        if index == 0:
            # print(f"index 0")
            if flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                return True
            
        elif index == len(flowerbed) - 1:
            # print(f"index == len(flowerbed)")
            if flowerbed[index] == 0 and flowerbed[index - 1] == 0:
                return True
            
        else:
            # print(f"index != 0 or len(flowerbed)")
            if flowerbed[index] == 0 and flowerbed[index + 1] == 0 and flowerbed[index - 1] == 0:
                return True
            
        return False
    
    def fillTestArray(self, flowerbed: List[int]) -> List[int]:
        return_array = flowerbed
        print(f"ffffflowerbed {flowerbed}")
        counter = 0
        for i in range(0, len(return_array)):
                if self.isValidFlowerSpot(return_array, i):
                    print(f"True")
                    return_array[i] = 1
                    counter += 1
                    print(f"fbed {flowerbed}")
                    
        print(f"N: {counter}")
        print(f"fvvvvvvlowerbed {flowerbed}")
        return return_array
                    
        
            
def Main():
    print(f"")
    solution = Solution()
    test_variable = [0, 0, 0, 0, 1]
    solution.canPlaceFlowers(test_variable, 2)

Main() 
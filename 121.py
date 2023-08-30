from typing import List  # Import the List type hint

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """_summary_

        Args:
            prices (List[int]): Stores the price the stock is worth on a specific day

        Returns:
            int: Returns the maximum profit if stock is bought and sold optimally 
        """
        return_value = 0
        highest_optimal_index = -1
        lowest_optimal_index = -1
        
        for i in range(0, len(prices)):
            if prices[i] 
        
        
        
            
        print(f"r_v {return_value}")
        return return_value
    
    

def main():
    solution = Solution()
    test_variable = [7,6,4,3,1]
    solution.maxProfit(test_variable)

if __name__ == "__main__":
    main()

# First Attempt:
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         return_value = 0
#         values_after_bought = []
#         for i in range(0, len(prices)):
            
#             for j in range(i, len(prices)):
#                 values_after_bought.append(prices[j])
            
#             # print(f"{i} {values_after_bought}")
            
#             for j in range(1, len(values_after_bought)):
#                 # print(f"j:{j} {values_after_bought[j]}")
#                 if values_after_bought[j] - values_after_bought[0] > return_value:
#                     return_value = values_after_bought[j] - values_after_bought[0]
                    
#             values_after_bought = []
            
#         # print(f"r_v {return_value}")
#         return return_value
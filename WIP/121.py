from typing import List  # Import the List type hint

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """_summary_

        Args:
            prices (List[int]): Stores the price the stock is worth on a specific day

        Returns:
            int: Returns the maximum profit if stock is bought and sold optimally 
        """
        highest = 0
        lowest = prices[0]
        highest_index = 0
        lowest_index = 0
        
        for i in range(len(prices) - 1, -1, -1):
            print(prices[i])
            if highest < prices[i]:
                highest = prices[i]
                highest_index = i
            if lowest > prices[i]:
                lowest = prices[i]
                lowest_index = i
        
        print(f"L: {lowest} | H: {highest}")
        print(f"LI: {lowest_index} | HI: {highest_index}")

        if highest_index > lowest_index:
            return highest - lowest
        
    


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

# Second attempt
# return_value = 0
        
#         highest_optimal_index = -1
#         lowest_optimal_index = -1
#         highest_value = -1
#         lowest_value = prices[0]
        
#         for i in range(0, len(prices)):
#             if prices[i] > highest_value:
#                 highest_value = prices[i]
#                 highest_optimal_index = i
#                 print(f"highest_value {highest_value} | highest_optimal_index {highest_optimal_index}")
                
#             elif prices[i] < lowest_value:
#                 lowest_value = prices[i]
#                 lowest_optimal_index = i
#                 print(f"lowest_value {lowest_value} | lowest_optimal_index {lowest_optimal_index}")
        
#         if highest_optimal_index < lowest_optimal_index:
#             print(f"highest_optimal_index < lowest_optimal_index")
#             print(f"{highest_optimal_index} < {lowest_optimal_index}")
        
            
#         print(f"r_v {return_value}")
#         return return_value
    
#     def helper(self, prices: List[int]):
#         return_value = 0
        
#         highest_optimal_index = -1
#         lowest_optimal_index = -1
#         highest_value = -1
#         lowest_value = prices[0]
        
#         for i in range(0, len(prices)):
#             if prices[i] > highest_value:
#                 highest_value = prices[i]
#                 highest_optimal_index = i
#                 print(f"highest_value {highest_value} | highest_optimal_index {highest_optimal_index}")
                
#             elif prices[i] < lowest_value:
#                 lowest_value = prices[i]
#                 lowest_optimal_index = i
#                 print(f"lowest_value {lowest_value} | lowest_optimal_index {lowest_optimal_index}")
        
#         if highest_optimal_index < lowest_optimal_index:
#             print(f"highest_optimal_index < lowest_optimal_index")
#             print(f"{highest_optimal_index} < {lowest_optimal_index}")
        
            
#         print(f"r_v {return_value}")
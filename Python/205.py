from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """_summary_

        Args:
            s (str): String number one
            t (str): String number two

        Returns:
            bool: True, If the words are isomorphic
        """

        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}
        
        for char_s, char_t in zip(s, t):
            if char_s in s_dict:
                if s_dict[char_s] != char_t:
                    return False
                
            else:
                s_dict[char_s] = char_t
                    
            if char_t in t_dict:
                if t_dict[char_t] != char_s:
                    return False
                
            else:
                t_dict[char_t] = char_s
        print(f"s_dict {s_dict}")
        print(f"t_dict {t_dict}")            
        return True
        
                    
        
def main():
    solution = Solution()
    test_variable_a = "foo"
    test_variable_b = "bar"
    print(solution.isIsomorphic(test_variable_a, test_variable_b))
    
    
if __name__ == "__main__":
    main()
    
    
    #     list_s = self.generateList(s)
    #     list_t = self.generateList(t)
    #     print(f"s {list_s}")
    #     print(f"t {list_t}")
        
    #     converted_list_s = self.convertListToOccurrences(list_s)
    #     converted_list_t = self.convertListToOccurrences(list_t)
        
    #     print(f"Converted:\ns {converted_list_s}")
    #     print(f"t {converted_list_t}")
        
    #     print(f"{list_s == list_t}")
    #     return list_s == list_t
        
    
    # def generateList(self, s: str) -> List[int]:
    #     return_list = []
    #     for i in range(0, len(s)):
    #         return_list.append(ord(s[i]))
            
    #     return return_list
    
    # def convertListToOccurrences(self, list: List[int]) -> List[int]:
    #     """Converts a list of ints to a list of occurrences for each int

    #     Args:
    #         list (List[int]): Original list populated with numbers

    #     Returns:
    #         List[int]: New list of how many times the number occurred 
    #         in the index of the original number
    #     """
    #     return_list = []
        
    #     for i in range(0, len(list)):
    #         num_to_check = list[i]
    #         count = 0
            
    #         for j in range(0, len(list)):
    #             if list[j] == num_to_check:
    #                 count += 1
            
                    
    #         return_list.append(count)
            
    #     print(f"{return_list}")
    #     return return_list
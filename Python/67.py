class Solution:
    def addBinary(self, a: str, b: str) -> str:
        test_string = ""
        len_of_a = len(a)
        len_of_b = len(b)
        num_to_append = 0
        
        if len_of_a > len_of_b:
            num_to_append = len_of_a - len_of_b
            for i in range(0, num_to_append):
                test_string += "+"
            test_string += b
            b = test_string
                
        else:
            num_to_append = len_of_b - len_of_a
            for i in range(0, num_to_append):
                test_string += "+"
            test_string += a
            a = test_string
          
        print(f"a {a} | b {b}")  
        test_string = ""
        
        carry_bit = False
        
        # Calculator Logic, appending answer to test_string
        for i in range(len(a) - 1, -1, -1):
            print(f"\ni {i}")
            
            print(f"a[i] {a[i]} | b[i] {b[i]}")
            
            # if a = 1 and b = 1
            if (a[i] == "1") and (b[i] == "1"):
                print(f"a and b == 1 | carry_bit {carry_bit}")
                
                # if we are carrying over a bit
                if carry_bit == True:
                    test_string += "1"
                    carry_bit = True
                # We are not carrying a bit    
                else:
                    test_string += "0"
                    carry_bit = True
                
            # if a = 0 and b = 1 or vice versa
            if ((a[i] == "1") and (b[i] == "0")) or ((a[i] == "0") and (b[i] == "1")):
                print(f"a and b == 0 or 1")
                if carry_bit == True:
                    test_string += "0"
                    carry_bit = True
                else:
                    test_string += "1"
                    carry_bit = False
              
            # if a = 0 and b = 0
            if (a[i] == "0") and (b[i] == "0"):
                print(f"a and b == 0")
                if carry_bit == True:
                    test_string += "1"
                else:
                    test_string += "0"
                
                carry_bit = False
                
            # if a '+' is detected
            if (a[i] == "+") or (b[i] == "+"):
                if (a[i] == "+"):
                    print(f"a[i] == '+'")
                    
                    if carry_bit == False:
                        test_string += b[i]
                    
                    # carry_bit == True
                    else:
                        if(b[i] == "1"):
                            test_string += "0"
                            carry_bit = True
                        else:
                            test_string += "1"
                            carry_bit = False
                            
                if (b[i] == "+"):
                    print(f"b[i] == '+'")
                    if carry_bit == False:
                        test_string += a[i]
                    else: # Carry bit is True
                        if(a[i] == "1"):
                            test_string += "0"
                            carry_bit = True
                        else:
                            test_string += "1"
                            carry_bit = False
                            
                            
            print(f"i {i} test_string {test_string}")
        
        if carry_bit == True:
            print(f"adding last num to string")
            test_string += "1"
                        
        # Generate Binary in reverse order, reverse string to fix
        print(f"test_string before {test_string}")
        test_string = "".join(reversed(test_string))
        print(f"test_string after {test_string}")
        return test_string      

def main():
    solution = Solution()
    test_variable_a = "11"
    test_variable_b = "1"
    answer = "100"
    solution.addBinary(test_variable_a, test_variable_b)

#if __name__ == "__main__":
main()
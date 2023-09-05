class Solution:
    def hammingWeight(self, n: int) -> int:
        hex_num = str(hex(n))
        return_one = 0
        print(f"{hex_num}")
        
        for i in range(0, len(hex_num)):
            if hex_num[i] == "1":
                return_one += 1
            elif hex_num[i] == "2":
                return_one += 1
            elif hex_num[i] == "3":
                return_one += 2
            elif hex_num[i] == "4":
                return_one += 1
            elif hex_num[i] == "5":
                return_one += 2
            elif hex_num[i] == "6":
                return_one += 2
            elif hex_num[i] == "7":
                return_one += 3
            elif hex_num[i] == "8":
                return_one += 1
            elif hex_num[i] == "9":
                return_one += 2
            elif hex_num[i] == "a":
                return_one += 2
            elif hex_num[i] == "b":
                return_one += 3
            elif hex_num[i] == "c":
                return_one += 2
            elif hex_num[i] == "d":
                return_one += 3
            elif hex_num[i] == "e":
                return_one += 3
            elif hex_num[i] == "f":
                return_one += 4
            
        
        print(f"{return_one}")        
        return return_one
            
        

def main():
    solution = Solution()
    test_variable = 0b11110101000001000100001000001011
    solution.hammingWeight(test_variable)

if __name__ == "__main__":
    main()
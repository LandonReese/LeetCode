class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_counter = 0
        needle_index = 0

        if len(needle) > len(haystack):
            return -1
        
        for i in range(0, len(haystack)):
            starting_index = i
            print(f"Starting index: {starting_index}")
            if needle[needle_index] == haystack[i]:
                for j in range(i, len(needle) + i):
                    print(f"needle {needle[needle_index]} hays {haystack[j]}")
                    if needle[needle_index] == haystack[j]:
                        needle_counter = needle_counter + 1
                        needle_index = needle_index + 1
                        print(f"New Needle Count {needle_counter}")
                        print(f"New Needle Index {needle_index}")
                    
                    else:
                        needle_counter = 0
                        needle_index = 0

            if needle_counter == len(needle):
                return starting_index
            
        return -1

def main():
    solution = Solution()
    haystack = "mississippi"
    needle = "issipi"
    print(f"Index: {solution.strStr(haystack, needle)}")

if __name__ == "__main__":
    main()
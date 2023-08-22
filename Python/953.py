from typing import List  # Import the List type hint

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        inputs: words - a list of strings
                order - a list of characters representing an alphabet
        output: True  - if words is sorted lexicographically
                False - if not
        """
        length_of_words = len(words)
        
        # Traverse the list of words
        for i in range(0, length_of_words - 1):
            #print(f"words[i] = {words[i]} | words[i+1] = {words[i+1]} | Alphabetical? {self.isWordSortedLexicographically(words[i], words[i + 1], order)}")
            #print(f"Not: {not self.isWordSortedLexicographically(words[i], words[i+1], order)}")
            if not self.isWordSortedLexicographically(words[i], words[i+1], order):
                return False
        return True
    
    def isWordSortedLexicographically(self, first_word: str, second_word: str, word_order: str) -> bool:
        """
        inputs:     first_word  - string 1
                    second_word - string 2
                    word_order  - List of characters representing an alphabet
        outputs:    True  - If first_word < second_word, by degree of order
                    False - If not in lexicographic order
        """
        first_word_spaced = first_word
        second_word_spaced = second_word
        # print(f"1st: {first_word} 2nd: {second_word}")

        # Data Types
        first_word_length = len(first_word)
        second_word_length = len(second_word)
        longest_word_length = 0
        number_of_nulls = 0

        # Select Longest Word Length
        # If the first word is longer
        if first_word_length > second_word_length:
            longest_word_length = first_word_length
            number_of_nulls = longest_word_length - second_word_length
            for i in range(0, number_of_nulls):
                second_word_spaced += "+"
        # If second word is longer
        else:
            longest_word_length = second_word_length
            number_of_nulls = longest_word_length - first_word_length
            for i in range(0, number_of_nulls):
                first_word_spaced += "+"

        # print(f"Longest word length: {longest_word_length}")
        # print(f"# of Nulls: {number_of_nulls}")
        
        # print(f"Word1 {first_word_spaced}")
        # print(f"Word2 {second_word_spaced}")

        # Compare words to eachother lexicographically
        # i traverses the shortest word length
        for i in range(0, longest_word_length):
            # j traverses the alphabet
            first_letter = self.lexicographicLetterValue(first_word_spaced[i], word_order)
            second_letter = self.lexicographicLetterValue(second_word_spaced[i], word_order)

            # print(f"First {first_letter} Second {second_letter}")

            # larger the number, the further in the alphabet
            # If the first word is lower in the alphabet
            if(first_letter < second_letter):
                break

            # If the letters are the same
            if(first_letter == second_letter):
                continue
            # default and continue searching for letters
                
            # If the first word is later in the alphabet
            if(first_letter > second_letter):
                return False

        # # If all of the previous statements are proved, return true if the shortest word occurred first
        # if(first_word_length > second_word_length):
        #     return False

        return True
    
    def lexicographicLetterValue(self, letter: str, word_order: str) -> int:
        """
        inputs:  letter     - letter to be searched for in alphabet
                 word_order - alphabet
        outputs: returns an int of the alphabetical location of the letter
                 returns 0 for a "+" (null-terminating character)
                 returns 1-26 if the letter exists in the alphabet
                 returns -1 otherwise
        """
        # print(f"Letter: {letter}")
        for i in range(0, len(word_order)):
                if(letter == "+"):
                    return 0
                if(letter == word_order[i]):
                    # print(f"Letter found: {word_order[i]}")
                    return i+1
        return -1

def main():
    solution = Solution()
    word_list = ["app","applause", "apple"]
    order_list = "aplebcdfghijkmnoqrstuvwxyz"

    print(f"Words in list: {len(word_list)} \nAlphabet -> {order_list}")

    print(f"isAlienSorted {solution.isAlienSorted(word_list, order_list)}")

if __name__ == "__main__":
    main()

# In an alien language, surprisingly, they also use English lowercase letters, 
# but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, 
# return true if and only if the given words are sorted lexicographically in this alien language.
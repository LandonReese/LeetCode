# Write a program that prints the numbers 1 to 100. If the number is a multiple of three, 
# print "Fizz" instead of the number. if the number is a multiple of five, print "Buzz" 
# instead of the number. If the number is a multiple of three and five, print "FizzBuzz" 
# instead of the number.


def fizzBuzz(num:int):
    for i in range(1, num + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

def main():
    number = 100
    fizzBuzz(number)

if __name__ == "__main__":
    main()

# for(int i = 1; i <= 100; i++;){

# }
"""
Print out the first 12 numbers of the fibonacci sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...
https://www.mathsisfun.com/numbers/fibonacci-sequence.html
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  There is more than one way to code a solution to this.
    #  The following steps give you some guidelines for one of them.
    #  1. Declare and initialize three int variables: number1, number2,
    #     and sum.
    number1 = 0
    number2 = 1
    sum = number1 + number2
    #  2. Initialize number1 and number2 to the first two numbers of the
    #     fibonacci sequence (0 and 1) and print both numbers.
    print(number1)
    print(number2)
    #  3. Use a for loop that calculates the sum of the two numbers and
    #     prints it. The for loop should repeat 10 times.
    for i in range(10):
        sum = number1 + number2
        print(sum)
        number1 = sum
        sum = number1 + number2
        print(sum)
        number2 = sum
    #  4. Now try to figure out how to change the variables before the for
    #     loop repeats so the sequence of numbers is correct.
    pass

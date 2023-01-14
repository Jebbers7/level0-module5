"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user for a number
    number = simpledialog.askinteger("Number", "Input a number.")
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    prime = True
    for i in range(number - 3):
        if number % (i + 2) == 0:
            prime = False
            messagebox.showinfo("Prime", "This number is not prime")
            exit()
        else:
            prime = True
        i += 1
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    messagebox.showinfo("Prime", "This number is prime")
    pass

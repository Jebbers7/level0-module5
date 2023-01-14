"""
Write an algorithm to change a string into a "goofy" version.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #  1. Ask the user to enter their name.
    name = simpledialog.askstring("Name", "What's your name?")
    #  2. Use a loop to alternately modify each character of the name into
    #     uppercase and lowercase letters until a new "goofy" representation
    #     of their name has been constructed.
    #     For example, if they enter their name as Alexander Hamilton
    #     their goofy name will be AlExAnDeR HaMiLtOn
    for i in range(len(name)):
        if i % 2 == 0:
            name[i] = name[i].upper()
        else:
            name[i] = name[i].lower()
    #  3. Show the user the goofy version of their name in a pop-up.
    messagebox.showinfo("Goofy Name", "Your goofy name is " + name)
    pass

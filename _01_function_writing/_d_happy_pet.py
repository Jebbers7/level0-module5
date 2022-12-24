"""
Write methods to represent the activities that will make the user's pet happy.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO)
    #   1. Ask the user to enter the type of pet they want (give them a few
    #      choices).
    answer = simpledialog.askstring(title="Pet", prompt="What type of pet do you want - Dog, Snake, or Fish?")
    #   2. Use a loop (maybe a while loop?) to keep offering interactions with
    #      their pet until the desired pet happiness level has been reached.
    #      Examples of activities are: Feed, Walk, Play
    petHappiness = 0
    def petActivity(pet, activity):
        petHappiness = 0
        if pet == 'Dog':
            if activity == 'Feed':
                petHappiness += 5
            elif activity == 'Walk':
                petHappiness += 10
            elif activity == 'Play':
                petHappiness += 25
        if pet == 'Snake':
            if activity == 'Feed':
                petHappiness += 10
            elif activity == 'Tap on glass':
                petHappiness += 5
            elif activity == 'Wrap around neck':
                petHappiness += 15
        if pet == 'Fish':
            if activity == 'Feed':
                petHappiness += 15
            elif activity == 'Filter water':
                petHappiness += 10
            elif activity == 'Buy a friend':
                petHappiness += 50
        return petHappiness


    while petHappiness < 50:
        choice = simpledialog.askstring("Activity", "What interaction do you want to do?")
        petHappiness = petHappiness + petActivity(answer, choice)
    #   3. Write a method for each of the pet activities offered.
    #      Each activity should increase (or decrease) the pet's happiness
    #      level by a different amount, depending on the kind of pet they
    #      have. For example, a fish might not enjoy a walk!




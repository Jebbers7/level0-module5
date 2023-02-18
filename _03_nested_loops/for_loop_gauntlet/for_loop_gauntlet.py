"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    for i in range(101):
        print(i)

    for i in range(101):
        print(100-i)

    for i in range(101):
        if i % 2 == 0:
            print(i)

    for i in range(100):
        if i % 2 == 1:
            print(i)

    for i in range(501):
        if i % 2 == 0:
            print(str(i) + " is even")
        elif i % 2 == 1:
            print(str(i) + " is odd")

    for i in range(778):
        if i % 7 == 0:
            print(i)

    for i in range(16):
        print("In " + str(i + 2007) + ", I was " + str(i) + " years old")

    for i in range(3):
        for j in range(3):
            print(str(i) + " " + str(j))

    j = 0
    for i in range(3):
        print(str(j + 1) + " " + str(j + 2) + " " + str(j + 3))
        j += 3
        i += 1

    for i in range(10):
        print("")
        for j in range(1,11):
            print(str(j + (i*10)), end=" ")

    for i in range(7):
        print("")
        for j in range(i):
            print("*", end="")

    print("")

    for i in range(101):
        print(str(100 - i))


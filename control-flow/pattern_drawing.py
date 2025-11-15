num = int(input("Enter the size of the pattern:"))

rows = 1

while rows <= num:

    i = 1
    for i in range(1, num+1) :
        print("*", end="")

    print()
    rows += 1
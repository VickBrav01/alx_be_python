pattern_size = int(input("Enter the size of the pattern:"))
row = 0
while row <= pattern_size:
    for row in range(pattern_size):
        for value in range(pattern_size):
            print("*", end=" ")
            row += 1
        print()
    
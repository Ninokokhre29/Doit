def print_pattern(x):
    i = 1
    while i <= x:
        for j in range(1, i + 1):
            print(j, end="")
        print()
        i += 1

print_pattern(5)



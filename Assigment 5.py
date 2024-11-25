#1

lst = ["apple", "banana", "cherry", "peach", "kiwi"]
from random import choice
x = choice(lst)

while True:
    ans = input("Insert Word: ")
    if ans != x:
        print("Keep Guessing")
    else:
        print("You Guessed the Word")
        break

#2

my_list = [43, '22', 12, 66, 210, ["hi"]]

print(my_list.index(210))
my_list[-1].append("hello")
my_list.remove(my_list[2])
print(my_list)
my_list_2 = my_list.copy()

#3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_0 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
for i in range(3):
    for j in range(3):
        matrix_0[i][j] = matrix[j][i]
print(matrix_0)

#1

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
y = int(input("How to change last value in tuple: "))
new_lst = []
for i in lst:
    x = list(i)
    x[-1] = y
    new_lst.append(x)
print(new_lst)

#2
st = {3, 17, 45, 67, 89, 23, 12, 78, 34, 56}
lst = list(sorted(st))
min = lst[0]
max = lst[-1]
print(f"მინიმალური მნიშვნელობა არის {min}, ხოლო მაქსიმალური მნიშვნელობა არის {max}")

#3

Input = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
Output = []
for i in Input:
    avg = sum(i)/len(i)
    Output.append(avg)
print(Output)

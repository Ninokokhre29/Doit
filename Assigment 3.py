#1
total_sum = 0
while True:
    num = input("რიცხვი: ")
    if num == "sum":
        print(total_sum)
        break
    elif int(num) > 0:
        total_sum += int(num)

#2
sum = 0
while True:
    num = int(input("რიცხვი:"))
    sum += num
    if num == 0:
        print(sum)
        break

#3
from random import randint
x = randint(1,10)
while True:
    num = int(input("გამოიცანი რიცხვი 1-დან 10-მდე: "))
    if num > x:
        print("გამოსაცნობი რიცხვი ამაზე ნაკლებია")
    elif num < x:
        print("გამოსაცნობი რიცხვი ამაზე მეტია")
    else:
        print("თქვენ სწორად გამოიცანით.")
        break






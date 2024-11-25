#1

def main(num = input("Write Number: ")):
    try:
        number = int(num)
        print(f"{num} is integer")
    except ValueError:
        print(f"{num} is not integer")

main()

#2
def divide(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print("0-ზე გაყოფა არ შეიძლება")

divide(10,2)


#3
Lst = ['hello', 'world', 'coding', 'nod']
End = "ing"

def main2(lst, end):
    new_lst = filter(lambda i: i[-len(end):] == end, lst)
    print(list(new_lst))

main2(Lst, End)



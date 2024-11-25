#1
lst = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
with open("file.txt", "w") as file:
    for i in lst:
        file.write(f"{i}\n")

#2
lst = ["red", "Green", "white", "Black", "Pink", "Yellow"]
with open("file2.txt", "w") as file:
    for i in lst:
        file.write(f"{i}\n")
with open("file2.txt", "r") as file2:
    count = 0
    for i in file2.readlines():
        if i[0].isupper():
            count += 1
print(f"მაღალ რეგისტრში დაწერილი სიტყვების რაოდენობა: {count}")



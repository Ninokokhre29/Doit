#1
score = int(input("შეიყვანეთ ქულა:"))
if score >= 91 and score <=100:
    print("A")
elif score >= 81 and score <= 90:
    print("B")
elif score >= 71 and score <= 80:
    print("C")
elif score >= 61 and score <= 70:
    print("D")
elif score >= 51 and score <= 60:
    print("E")
#2
num = int(input("შეიყვანეთ რიცხვი:"))
if num % 2 == 0:
    print("ლუწი")
else:
    print("კენტი")
#3
sen = input("დაწერეთ წინადადება: ")

if "small" in sen:
    print("small")
elif "middle" in sen:
    print("middle")
elif "tall" in sen:
    print("tall")
else:
    print("ტექსტში ეს სამი სიტყვა არ მოიძებნა")
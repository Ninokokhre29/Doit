#1
name = input("word:")
reverse_name = name[::-1]
print(name == reverse_name)

#2
txt = input("write text:")
for i in txt:
    print(ord(i))

#3
while True:
    name = input("word:")
    check = name[-3:]
    if name == "stop":
        break
    elif check == "ing":
        print(f"{name}ly")
    else:
        print(f"{name}ing")
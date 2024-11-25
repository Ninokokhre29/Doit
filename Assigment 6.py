#1
def main(num_1, num_2):
    lst = list(range(num_1, num_2 +1))
    return [i ** 2 for i in lst]

print(main(1,3))

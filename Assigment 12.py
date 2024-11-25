import csv

data = [["Full Name", "Subject", "Score"],
        ["Giorgi Gelashvili", "Mathematics", 90],
        ["Giorgi Gelashvili", "Chemistry", 10],
        ["Gela Gotsiridze", "Mathematics", 20],
        ["Gela Gotsiridze", "Chemistry", 20]]

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(data)

students_scores = {}

with open("data.csv", "r") as file:
    for row in csv.DictReader(file):
        name = row["Full Name"]
        score = int(row["Score"])
        if name not in students_scores:
            students_scores[name]=[]
        students_scores[name].append(score)

students_avg = {name: sum(scores) / len(scores) for name, scores in students_scores.items()}

print("სტუდენტის ქულა ", students_scores)
print("საშუალო ქულა ", students_avg)


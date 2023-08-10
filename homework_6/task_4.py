import json
import csv

phone_dict = {
    "Kirill": "123456789",
    "Oleg": "234567890",
    "Lesha": "345678901",
    "Liza": "456789012",
    "Alisa": "567890123"
}

with open('task_3.json', 'r') as my_file:
    data = json.load(my_file)
print(data)



with open('task_4.csv', 'w', newline="") as csvfile:
    cols = ['ID', 'Имя', 'Возраст', 'Телефон']
    writer = csv.DictWriter(csvfile, fieldnames = cols)
    writer.writeheader()

    for id_num, (name, age) in data.items():
        phone = phone_dict.get(name,"")
        writer.writerow({'ID': id_num, 'Имя': name, 'Возраст': age, 'Телефон': phone})

import json


d = {

    111111:('Kirill', 22),
    222222:('Oleg', 25),
    333333:('Lesha', 30),
    444444:('Liza', 22),
    555555:('Alisa', 42)

}

with open('task_3.json', 'w') as my_file:
    json.dump(d, my_file)
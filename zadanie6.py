import json
import csv
with open('peson.json', 'r',encoding="UTF-8") as file:
    person = json.load(file)

# запись данных в файл csv
with open('person.csv', 'w') as file2:
    writer = csv.writer((file2),delimiter = ':')
    for key, value in person.items():
        writer.writerow(['person', key, value[0], value[1]])
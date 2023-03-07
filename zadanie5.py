import json
person = {
    12345: ("Mike", 25),
    54321: ("Ann", 32),
    67890: ("Peter", 47),
    98765: ("Maria", 18),
    54289: ("Victor", 21)
}
with open('peson.json', 'w', encoding='UTF-8') as file_person:
    json.dump(person,file_person,indent=2)
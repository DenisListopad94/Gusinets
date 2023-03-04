from datetime import datetime, timedelta
file3 = open('sklad.txt','r',encoding="UTF-8")
products = {}
for line in file3:
    lst = line.rstrip().split()
    characteristic = list(map(str, lst[1:]))
    products[lst[0]] = characteristic

file3.close()

today = datetime.now()

for name,characteristic in products.items():
    date = datetime.strptime(characteristic[2], '%Y-%m-%d')
    delta = today - date
    if int(characteristic[0])* int(characteristic[1]) > 1000000 and delta.days > 30 :
        print(name,characteristic)
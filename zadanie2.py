file = open('input.txt', 'w', encoding='UTF-8')
file.write('10 20 65 19 123 43 91 87 66 95')
file.close()

file = open('input.txt', 'r', encoding='UTF-8')
some_numb = file.read()
file.close()
print(some_numb)

numbers = list(map(int, some_numb.split()))
file1 = open('output.txt', 'w', encoding="UTF-8")
n = 1
for elem in numbers:
    n *= elem
file1.write(str(n))
file1.close()
import re
#zadanie1
# stroka = 'Cat catfish cathz dog cat mouse'
# print(re.findall(r'cat', stroka, re.IGNORECASE))


#zadanie2
# pattern = r'z...z'
# stroka = 'z???z z777z zero zebrz zona z)))z'
# print(re.findall(pattern,stroka))

#zadanie3
# pattern = r'(?:\+8|9)(?:-\d{3}){3}'
# stroka = '+8-789-318-430 +3-814-561-990 9-670-439-222 +375-44-680-04-14 +87-345-233-444'
# print(re.findall(pattern, stroka))

#zadanie4
# pattern = r'\b[aeyuio]\w+'
# stroka = 'camp icon Elephant angry oak bear'
# words = re.findall(pattern, stroka, re.IGNORECASE)
# print(words)

#zadanie5
# pattern = r'[+-]?\d+'
# stroka = '28 tiger 2 -143 hello -20 31 1001'
# print(re.findall(pattern,stroka))

#zadanie6
# stroka = 'I am a human, you know! Hello human'
# print(re.sub('human', 'computer', stroka))

#zadanie7
# pattern = r'\b\d\d-\d\d-\d{4}\b'
# stroka = '223 28-10-2001 222-04-1999 fact 23-02-20111 hello 11-09-2002'
# print(re.findall(pattern,stroka))


#zadanie8
# pattern = r'\w*b\w*'
# stroka = 'bear fox cat baby copybook lamp climb'
# print(re.findall(pattern,stroka))

#zadanie9
# pattern = r'(\w)\1+'
# repl = r'\1'
# stroka = 'worldddd weathhhhher laptoppp fffly'
# print(re.sub(pattern,repl,stroka))
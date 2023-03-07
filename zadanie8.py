with open('8.txt', 'r',encoding="UTF-8") as file:
    text = file.readline()

nums = []
letters = []
for i in range(len(text)):
    if text[i].isdigit():
        nums.append(int(text[i]))
    else:
        letters.append(text[i])

new_text = ''
for i in range(len(letters)):
    new_text += letters[i] * nums[i]

print(new_text)

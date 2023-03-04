with open('7.txt', 'r',encoding="UTF-8") as file7:
    text = file7.read()

words = text.lower().split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

most_word = ''
most_count = 0
for word, count in word_counts.items():
    if count > most_count or (count == most_count and word < most_word):
        most_word = word
        most_count = count

# выводим результаты
print(most_word, most_count)
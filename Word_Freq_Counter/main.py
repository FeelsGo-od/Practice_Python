from collections import Counter

text = input("Write your text to count frequency of each word: ")

words = text.split()

word_counts = Counter(words)

for word, count in word_counts.items():
    print(f"{word}: {count}")
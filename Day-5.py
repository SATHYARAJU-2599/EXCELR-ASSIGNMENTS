#write a python progrm to claculate the frquency of each word ina given text print the words and corresponding counts

from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    word_counts = Counter(words) 

    for word, count in word_counts.items():
        print(f"{word}: {count}")
text = "Hello I am Sathya from Aiml Department."
word_frequency(text)


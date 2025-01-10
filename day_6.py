# Write a Python program to using NLTK and Spacy
# •	Convert text to lowercase.
# •	Remove stopwords using NLTK
from collections import Counter
import nltk
import spacy
nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
nlp = spacy.load("en_core_web_sm")
def word_frequency(text):
    doc = nlp(text.lower())
    words = [token.text for token in doc]
    words = [word for word in words if word not in stop_words]
    word_counts = Counter(words)
    for word, count in word_counts.items():
        print(f"{word}: {count}")
text = "Hello I am Sathya from Aiml Department."
word_frequency(text)


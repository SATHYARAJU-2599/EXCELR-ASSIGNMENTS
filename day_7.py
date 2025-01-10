#  Write a Python script that:
# 1. Use Genism to preprocess data from a sample text file, follow basic procedures like tokenization, stemming, lemmatization etc.

from collections import Counter
import nltk
import spacy
from gensim.utils import simple_preprocess

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')

stop_words = nltk.corpus.stopwords.words('english')
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):

    # 1. Tokenization using Gensim
    tokens = simple_preprocess(text.lower())

    # 2. Remove stopwords
    tokens = [token for token in tokens if token not in stop_words]
    doc = nlp(" ".join(tokens))
    lemmas = [token.lemma_ for token in doc if not token.is_stop]
    return lemmas
text = "Hello I am Sathya from Aiml Department."

preprocessed_tokens = preprocess_text(text)
print(preprocessed_tokens)
word_counts = Counter(preprocessed_tokens)
for word, count in word_counts.items():
    print(f"{word}: {count}")

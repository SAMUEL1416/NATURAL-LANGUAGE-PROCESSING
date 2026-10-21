
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = [
    "playing", "played", "plays",
    "studies", "studying", "connected",
    "connection", "relational", "happiness"
]

for word in words:
    print(word, "->", stemmer.stem(word))

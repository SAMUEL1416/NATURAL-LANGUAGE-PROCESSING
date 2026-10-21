
import nltk

nltk.download("punkt_tab", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

text = "The student is studying natural language processing"

tokens = nltk.word_tokenize(text)
tagged_words = nltk.pos_tag(tokens)

print("Word\tPOS Tag")
for word, tag in tagged_words:
    print(word, "\t", tag)

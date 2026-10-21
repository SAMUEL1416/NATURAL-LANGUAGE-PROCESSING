
import nltk
from nltk.tag import RegexpTagger

patterns = [
    (r"the|a|an", "DT"),
    (r".*ing$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*ly$", "RB"),
    (r".*ous$|.*ful$|.*ive$", "JJ"),
    (r".*s$", "NNS"),
    (r".*", "NN")
]

tagger = RegexpTagger(patterns)

words = [
    "the", "student", "playing",
    "walked", "quickly", "beautiful"
]

tagged = tagger.tag(words)

for word, tag in tagged:
    print(word, "->", tag)

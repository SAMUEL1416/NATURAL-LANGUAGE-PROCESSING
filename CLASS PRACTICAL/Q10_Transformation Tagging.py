
# Initial tagging
words = ["The", "dogs", "are", "running", "quickly"]

tagged = [
    ("The", "NN"),
    ("dogs", "NN"),
    ("are", "NN"),
    ("running", "NN"),
    ("quickly", "NN")
]

print("Before transformation:")
print(tagged)

# Transformation rules
for i, (word, tag) in enumerate(tagged):

    # Rule 1: "The" is a determiner
    if word.lower() in ["the", "a", "an"]:
        tagged[i] = (word, "DT")

    # Rule 2: Words ending in "ing" are tagged as VBG
    elif word.endswith("ing"):
        tagged[i] = (word, "VBG")

    # Rule 3: "are" is a verb
    elif word.lower() == "are":
        tagged[i] = (word, "VBP")

    # Rule 4: Words ending in "ly" are tagged as adverbs
    elif word.endswith("ly"):
        tagged[i] = (word, "RB")

print("\nAfter transformation:")
print(tagged)

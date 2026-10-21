
import random
from collections import defaultdict, Counter

dataset = [
    "the cat sat on the mat",
    "the cat ate the fish",
    "the dog sat on the floor",
    "the dog ate the food",
    "a student reads a book",
    "a student writes a program",
    "the teacher teaches the students",
    "the students learn new concepts",
    "the bird flies in the sky",
    "the sun shines in the sky",
    "the moon shines at night",
    "the boy plays with a ball",
    "the girl reads an interesting book",
    "the computer processes the data",
    "the teacher explains the lesson",
    "the student learns new concepts",
    "the dog plays in the garden",
    "the cat sleeps on the sofa",
    "the children play in the park",
    "the farmer grows fresh vegetables"
]

bigrams = defaultdict(Counter)

for sentence in dataset:
    words = ["<START>"] + sentence.lower().split() + ["<END>"]

    for i in range(len(words) - 1):
        bigrams[words[i]][words[i + 1]] += 1

def generate_sentence():
    current = "<START>"
    result = []

    for _ in range(15):
        choices = bigrams.get(current)

        if not choices:
            break

        # Select a likely next word based on training frequency
        words = list(choices.keys())
        weights = list(choices.values())
        current = random.choices(words, weights=weights, k=1)[0]

        if current == "<END>":
            break

        result.append(current)

    return " ".join(result).capitalize() + "."

random.seed(10)

print("Generated Sentences:")
for i in range(5):
    print(i + 1, generate_sentence())

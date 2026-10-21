
from collections import defaultdict, Counter

# Training corpus: (word, POS tag)
training_data = [
    [("the", "DT"), ("cat", "NN"), ("runs", "VBZ")],
    [("a", "DT"), ("dog", "NN"), ("runs", "VBZ")],
    [("the", "DT"), ("dog", "NN"), ("sleeps", "VBZ")],
    [("a", "DT"), ("cat", "NN"), ("sleeps", "VBZ")]
]

word_tag_counts = defaultdict(Counter)
tag_counts = Counter()

for sentence in training_data:
    for word, tag in sentence:
        word_tag_counts[word][tag] += 1
        tag_counts[tag] += 1


def stochastic_tagger(sentence):
    result = []

    for word in sentence.lower().split():
        if word in word_tag_counts:
            tag = word_tag_counts[word].most_common(1)[0][0]
        else:
            tag = "NN"  # Default for unknown words

        result.append((word, tag))

    return result


sentence = "the cat runs"
print(stochastic_tagger(sentence))


def morphological_analysis(word):
    irregular = {
        "better": "good",
        "best": "good",
        "went": "go",
        "children": "child",
        "mice": "mouse",
        "leaves": "leaf"
    }

    if word in irregular:
        return irregular[word]

    # Derivational forms
    if word == "happiness":
        return "happy"
    if word == "relational":
        return "relate"
    if word == "connection":
        return "connect"

    # Verb forms ending in -ied
    if word.endswith("ied") and len(word) > 3:
        return word[:-3] + "y"

    # Common -ing forms
    if word.endswith("ing") and len(word) > 4:
        root = word[:-3]

        if len(root) > 1 and root[-1] == root[-2]:
            root = root[:-1]

        if root in ["stud", "cry", "fly", "try"]:
            root = root + "y" if root == "stud" else root

        return root

    # Common -ed forms
    if word.endswith("ed") and len(word) > 3:
        root = word[:-2]

        if len(root) > 1 and root[-1] == root[-2]:
            root = root[:-1]

        if root.endswith("i"):
            root = root[:-1] + "y"

        return root

    # Plural nouns
    if word.endswith("ies") and len(word) > 3:
        return word[:-3] + "y"

    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]

    return word


dataset = [
    "playing", "played", "studied", "studies", "running",
    "happiness", "cars", "connected", "connection",
    "better", "flying", "dogs", "relational",
    "crying", "leaves"
]

print(f"{'Word':<20}{'Root Form':<20}")
print("-" * 40)

for word in dataset:
    print(f"{word:<20}{morphological_analysis(word):<20}")

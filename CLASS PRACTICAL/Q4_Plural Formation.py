
def plural(noun):
    if noun.endswith(("s", "sh", "ch", "x", "z")):
        return noun + "es"
    elif noun.endswith("y") and len(noun) > 1:
        if noun[-2].lower() not in "aeiou":
            return noun[:-1] + "ies"
    return noun + "s"


words = ["cat", "bus", "box", "baby", "book", "dish"]

for word in words:
    print(word, "->", plural(word))

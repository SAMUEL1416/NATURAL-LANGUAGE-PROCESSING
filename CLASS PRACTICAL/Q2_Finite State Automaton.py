
def accepts(string):
    state = 0

    for ch in string:
        if ch not in "ab":
            return False

        if state == 0:
            state = 1 if ch == "a" else 0
        elif state == 1:
            state = 1 if ch == "a" else 2
        elif state == 2:
            state = 1 if ch == "a" else 0

    return state == 2


strings = ["ab", "aab", "bab", "aba", "abb", "aa"]

for s in strings:
    if accepts(s):
        print(s, "Accepted")
    else:
        print(s, "Rejected")

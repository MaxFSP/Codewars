def duplicate_count(text):
    one = []
    dif = []
    c=0
    text = text.lower()
    for letters in text:
        if letters not in one:
            one.append(letters)
        else:
            if letters not in dif:
                dif.append(letters)
                c+=1
    return c
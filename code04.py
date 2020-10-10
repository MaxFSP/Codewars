def printer_error(s):
    allowed = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    c = 0
    c1 = 0
    for i in s:
        if i in allowed:
            c1+=1
            continue
        else:
            c1+=1
            c +=1
    return str(str(c)+"/"+str(c1))
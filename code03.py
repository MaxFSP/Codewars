def persistence(n):
    count = 0
    while len(str(n)) > 1:
        output = 1
        for x in str(n):
            output *= int(x)
        count += 1
        n = output
    return count
def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    i = 0
    val = iterable[0]
    unique = [val]
    while i < len(iterable) - 1:
        if iterable[i+1] == val:
            i += 1
        else:
            val = iterable[i+1]
            unique.append(val)
    return unique
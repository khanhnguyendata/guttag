def intersect(t1, t2):
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)

    return result

print(intersect((1, 2, 3), (2, 3, 4)))